"""
Split curriculum.yaml into index + per-chapter files using line-based parsing.
Avoids yaml.safe_load issues with malformed flow sequences in source file.
"""
import os, re, yaml

SRC = os.path.join(os.path.dirname(__file__), '..', 'references', 'curriculum.yaml')
CHAPTERS_DIR = os.path.join(os.path.dirname(__file__), '..', 'references', 'chapters')
INDEX_OUT = os.path.join(os.path.dirname(__file__), '..', 'references', 'curriculum_index.yaml')

os.makedirs(CHAPTERS_DIR, exist_ok=True)

slug_map = {
    1: 'fundamentals', 2: 'strings', 3: 'numbers', 4: 'booleans',
    5: 'conditionals', 6: 'loops', 7: 'data-structures', 8: 'functions',
    9: 'file-io', 10: 'csv-processing', 11: 'file-automation', 12: 'first-money'
}

with open(SRC, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# --- Parse top-level metadata (lines before 'chapters:') ---
header_lines = []
chapters_start = 0
for i, line in enumerate(lines):
    if line.strip() == 'chapters:':
        chapters_start = i + 1
        break
    header_lines.append(line)

header_text = ''.join(header_lines)
header = yaml.safe_load(header_text)  # safe: no special chars in header

# --- Split raw chapter blocks ---
# Chapters start with "- id: N" at 0-indent under chapters:
chapter_blocks = []
current_block = []
chapter_id_re = re.compile(r'^- id: (\d+)\s*$')

for line in lines[chapters_start:]:
    m = chapter_id_re.match(line)
    if m and current_block:
        chapter_blocks.append(current_block)
        current_block = [line]
    elif m:
        current_block = [line]
    else:
        current_block.append(line)
if current_block:
    chapter_blocks.append(current_block)

print(f"Found {len(chapter_blocks)} chapters")

# --- Extract metadata from each chapter for index ---
def extract_re(block_text, key):
    m = re.search(rf'^\s{{2,4}}{key}:\s*(.+)$', block_text, re.MULTILINE)
    return m.group(1).strip().strip('"\'') if m else ''

def extract_lessons_meta(block_text):
    """Extract id/title/objective/duration per lesson using regex."""
    lessons = []
    # Lessons start with "  - id: N" (2-space indent under chapter)
    lesson_blocks = re.split(r'(?=\n {2}- id: \d+)', '\n' + block_text)
    lesson_re = re.compile(r'- id: (\d+)')
    for lb in lesson_blocks:
        m = lesson_re.search(lb)
        if not m:
            continue
        lid = int(m.group(1))
        title = extract_re(lb, 'title')
        objective = extract_re(lb, 'objective')
        dur_m = re.search(r'duration_minutes:\s*(\d+)', lb)
        duration = int(dur_m.group(1)) if dur_m else 0
        prereq_m = re.search(r'prerequisites:\s*(\[.*?\])', lb)
        prereqs = prereq_m.group(1) if prereq_m else '[]'
        lessons.append({
            'id': lid, 'title': title,
            'objective': objective,
            'duration_minutes': duration,
        })
    return lessons

index_chapters = []
for block in chapter_blocks:
    block_text = ''.join(block)
    ch_id = int(re.search(r'^- id: (\d+)', block_text).group(1))
    slug = slug_map.get(ch_id, f'ch{ch_id:02d}')
    filename = f'ch{ch_id:02d}-{slug}.yaml'

    # Write raw chapter file (preserve original YAML text)
    chapter_path = os.path.join(CHAPTERS_DIR, filename)
    with open(chapter_path, 'w', encoding='utf-8') as f:
        f.writelines(block)

    # Build index entry
    title = extract_re(block_text, 'title')
    description = extract_re(block_text, 'description')
    lessons_meta = extract_lessons_meta(block_text)

    index_chapters.append({
        'id': ch_id,
        'title': title,
        'description': description,
        'file': f'chapters/{filename}',
        'lessons': lessons_meta,
    })

    lines_count = len(block)
    print(f"  ch{ch_id:02d} ({slug}): {lines_count} lines, {len(lessons_meta)} lessons")

# --- Write index YAML ---
index = {
    'curriculum_version': header.get('curriculum_version'),
    'curriculum_name': header.get('curriculum_name'),
    'delivery_mode': header.get('delivery_mode'),
    'total_lessons': header.get('total_lessons'),
    'usage': (
        'Load this index for navigation/trigger. '
        'For full lesson content, read the chapter file listed in each chapter.file field.'
    ),
    'chapters': index_chapters,
}

with open(INDEX_OUT, 'w', encoding='utf-8') as f:
    yaml.dump(index, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

with open(INDEX_OUT, encoding='utf-8') as f:
    idx_lines = f.read().count('\n')

total_ch_lines = sum(len(b) for b in chapter_blocks)
print(f"\nDone.")
print(f"  curriculum_index.yaml : {idx_lines} lines  ({idx_lines*100//3122}% of original)")
print(f"  chapters/ total       : {total_ch_lines} lines")
print(f"  Largest chapter load  : ~{max(len(b) for b in chapter_blocks)} lines (vs 3122 before)")
