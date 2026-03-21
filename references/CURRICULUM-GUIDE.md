# Curriculum Guide for AI Agents

## File Structure

```
references/
  curriculum.yaml              ← SOURCE OF TRUTH — chỉ edit file này
  curriculum_index.yaml        ← Auto-generated. ĐỪNG edit tay.
  chapters/
    ch01-fundamentals.yaml     ← Auto-generated. ĐỪNG edit tay.
    ch02-strings.yaml
    ch03-numbers.yaml
    ch04-booleans.yaml
    ch05-conditionals.yaml
    ch06-loops.yaml
    ch07-data-structures.yaml
    ch08-functions.yaml
    ch09-file-io.yaml
    ch10-csv-processing.yaml
    ch11-file-automation.yaml
    ch12-first-money.yaml
```

---

## Khi nào đọc file nào

| Mục đích | File cần đọc |
|---|---|
| Biết curriculum có gì, chapter nào, lesson nào | `curriculum_index.yaml` (~336 dòng) |
| Dạy 1 bài cụ thể | `chapters/chXX-name.yaml` cho chapter đó |
| Sửa nội dung bài học | `curriculum.yaml` (xem mục Update bên dưới) |

**Không bao giờ đọc `curriculum.yaml` trực tiếp khi dạy** — 3122 dòng, quá lớn, tốn context.

---

## Quy trình Update Curriculum

### Bước 1 — Edit source of truth

Mở `references/curriculum.yaml` và sửa theo ý muốn:
- Thêm/sửa/xóa lesson
- Sửa explanation, examples, exercise
- Thêm chapter mới

**Lưu ý YAML:** Nếu dùng dấu `>`, `<`, `[`, `]` bên trong flow sequence `[...]`, phải đặt trong quotes:
```yaml
# SAI — yaml lỗi
concepts_used: [comparison (>=, >), bool]

# ĐÚNG
concepts_used: ["comparison (>=, >)", "bool"]
```

### Bước 2 — Regenerate index + chapters

```bash
python scripts/split_curriculum.py
```

Script sẽ:
- Tạo lại `curriculum_index.yaml` từ đầu
- Tạo lại toàn bộ 12 file trong `chapters/`
- In summary số dòng mỗi chapter

### Bước 3 — Xong

Không cần làm gì thêm. Skill sẽ tự dùng index + chapter files đã update.

---

## Thêm Chapter Mới

1. Thêm chapter vào `curriculum.yaml` với format chuẩn (xem các chapter hiện có)
2. Thêm slug cho chapter mới vào `slug_map` trong `scripts/split_curriculum.py`:
   ```python
   slug_map = {
       ...,
       13: 'ten-chapter-moi',
   }
   ```
3. Chạy `python scripts/split_curriculum.py`

---

## Khi Script Báo Lỗi

**`yaml.scanner.ScannerError`** — có ký tự đặc biệt chưa được quote trong `curriculum.yaml`.
Xem dòng lỗi được báo, tìm flow sequence `[...]` chứa `>`, `<`, `[`, `]` và thêm quotes.

**`UnicodeDecodeError`** — đọc file không dùng UTF-8. Đảm bảo mở file với `encoding='utf-8'`.
