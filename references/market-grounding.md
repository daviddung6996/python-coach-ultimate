# Market grounding notes for Python coach

Mục tiêu: tránh ví dụ/monetization kiểu AI-generic. Chỉ dùng case có thể kiểm chứng.

---

## 1. Public freelance/job signals (2026-03-20)

### Verified market signals

Các tín hiệu dưới đây đã xem trực tiếp bằng browser tool:

- Freelancer Python jobs — https://www.freelancer.com/jobs/python/
  - Verify: title `Python Jobs for March 2026 | Freelancer`
  - Verify: `282 jobs found`
  - Signal trên page: automated tools for data gathering, cleaning, analysis; customized reports; Flask/Django; ML.

- Freelancer Excel jobs — https://www.freelancer.com/jobs/excel/
  - Verify: title `Excel Jobs for March 2026 | Freelancer`
  - Verify: `446 jobs found`
  - Signal trên page: customized templates for reporting, data entry/organization, data extraction, fixing existing Excel files, retyping docs into spreadsheets, web scraping for further analysis.

### Market verdict cho first-money track

Kết luận thẳng:
- Đường ngắn nhất tới job local 300k-500k không phải web app, không phải AI, cũng chưa phải scraper nặng.
- Track gần tiền nhất là: xử lý file + clean CSV/Excel + report đơn giản + rename file hàng loạt.
- Vì vậy lesson 7-15 phải ưu tiên task kiểu list/filter/sort/combine gắn với rows, filenames, order lines, report lines; không dạy demo toy nếu có lựa chọn thực dụng hơn.

### Channel reliability

- Freelancer đủ tốt để lấy tín hiệu nhu cầu public và nhóm task phổ biến.
- Board VN như TopCV / VietnamWorks / Glints bị bot protection trong phiên browser hiện tại, nên **không dùng board VN bị chặn làm anchor cho giá hay claim cụ thể**.
- Upwork search cũng bị chặn trong phiên này (`Just a moment...` / Cloudflare), nên không dùng làm evidence chính.
- Với thị trường VN, chỉ dùng framing mức giá bảo thủ cho first-money local: 300k-500k cho task nhỏ, khi scope rõ, input/output đơn giản, không cần maintain dài hạn.
- Kết luận: market evidence hiện đủ để nói `task family nào có nhu cầu`, nhưng chưa đủ để claim `job link VN cụ thể` trong mọi bài. Nếu chưa verify được job post thật, chỉ nói theo task family + range bảo thủ.

### First-money task ladder

1. `clean_names.py` — chuẩn hóa tên khách/sản phẩm.
2. `sum_orders.py` — cộng doanh thu từ list hoặc CSV nhỏ.
3. `find_invalid_rows.py` — tìm dòng lỗi, thiếu dữ liệu.
4. `rename_files.py` — đổi tên file theo pattern.
5. `simple_report.py` — xuất báo cáo text/CSV rõ ràng.

Common roles/tín hiệu phù hợp cho người mới:
- Data cleanup nội bộ
- Excel reporting support
- File handling / document organization
- Ops automation nhẹ

---

## 2. Verified resource basket (3 nguồn)

### Official / course

Các page dưới đây đã verify trực tiếp bằng browser tool:
- Python Docs Tutorial — https://docs.python.org/3/tutorial/index.html
  - Verify: title `The Python Tutorial — Python 3.14.3 documentation`
  - Giá trị: chuẩn khái niệm nền, control flow, data structures.
- CS50P — https://cs50.harvard.edu/python/
  - Verify: title `CS50's Introduction to Programming with Python`
  - Verify: modules thấy rõ `Functions, Variables`, `Conditionals`, `Loops`, `File I/O`.
  - Giá trị: curriculum backbone cho beginner nghiêm túc.
- Real Python Start Here — https://realpython.com/start-here/
  - Verify: title `Become a Python Expert – Real Python`
  - Verify: nhấn mạnh `real-world examples` và guided learning.
  - Giá trị: nguồn viết dễ đọc, practical hơn docs thuần.

### Video

- Corey Schafer — `Python Tutorial: Automate Parsing and Renaming of Multiple Files`
  - https://www.youtube.com/watch?v=ve2pmm5JqmI
  - Verify: channel `Corey Schafer`, `453k views`, `1.52M subscribers`.
  - Giá trị: cực sát first-money task `rename_files.py`.

### GitHub

- trenton3983/Excel_Automation_with_Python
  - https://github.com/trenton3983/Excel_Automation_with_Python
  - Verify: repo public, `Star 50`, latest commit `Apr 1, 2025`, mô tả repo nói rõ automates Excel workflows on Windows using win32com.
  - Giá trị: rất sát bối cảnh Windows + report/pivot/formatting.

- fzumstein/python-for-excel
  - https://github.com/fzumstein/python-for-excel
  - Verify: repo public, `Star 746`, latest commit shown `Mar 12, 2026`; companion repo cho sách `Python for Excel`; có thư mục `csv`, `sales_data`, `xl`.
  - Giá trị: rất hợp để lấy sample gần task merge/report/Excel mà không quá enterprise.

- thepycoach/automation
  - https://github.com/thepycoach/automation
  - Verify: repo public, `Star 1k`, latest commit shown `May 19, 2024`; có thư mục `3.Excel Report` và `File Managment`.
  - Giá trị: basket mini-automation dễ map sang bài first-money hơn repo library thuần.

### Rule mới khi chọn repo/video

- Task-aligned > star count. Repo ít sao vẫn giữ nếu đúng job đầu tiên, code đọc được, và update chưa quá stale.
- Ưu tiên nguồn giúp learner làm `clean CSV / rename files / simple report / merge Excel` hơn là repo đẹp nhưng xa first-money.
- Tránh repo/tool có risk spam, abuse, hoặc quá enterprise so với trình độ hiện tại.

---

## 3. Case Studies Grounded (VN Context)

### Case 1: Shop nhỏ gộp báo cáo đơn hàng
**Nhu cầu:**
- Shop bán trên Shopee, Lazada, Tiki có 3 file Excel riêng.
- Cần gộp thành 1 file tổng để gửi kế toán cuối tuần.

**Solution:**
```python
import pandas as pd
import os

files = ['shopee.xlsx', 'lazada.xlsx', 'tiki.xlsx']
dfs = [pd.read_excel(f) for f in files]
combined = pd.concat(dfs, ignore_index=True)
combined.to_excel('bao_cao_tuan.xlsx', index=False)
```

**Deliverables:**
- Script `merge_orders.py`
- `requirements.txt` (pandas, openpyxl)
- README.md với hướng dẫn chạy
- Sample input/output files

**Pricing:** 500k - 1.5m VND (tùy độ phức tạp)

---

### Case 2: Price monitoring cho seller
**Nhu cầu:**
- Seller cần theo dõi giá 50 sản phẩm đối thủ trên Shopee.
- Chạy script mỗi sáng, nhận báo cáo qua email/Telegram.

**Tools:**
- `requests`, `BeautifulSoup`, `selenium` (nếu cần login)
- `smtplib` hoặc `python-telegram-bot`

**Deliverables:**
- Script `price_monitor.py`
- Config file (product URLs, thresholds)
- Cron job setup guide
- Sample report

**Pricing:** 1m - 3m VND + 500k/tháng (nếu maintain)

---

### Case 3: Clean CSV data cho data analyst
**Nhu cầu:**
- Data bị duplicate, format sai, missing values.
- Cần script chuẩn hóa trước khi nhập vào database.

**Tools:**
- `pandas`, `csv`, `re`

**Deliverables:**
- Script `clean_data.py`
- Input sample + expected output
- Log file (records cleaned, errors)

**Pricing:** 300k - 800k VND

---

## 4. Pricing Strategy (VN Context)

**Cảnh báo:** bảng dưới là `range bảo thủ để coaching`, không phải quote market scrape trực tiếp từng job post. Dùng để framing, không dùng như fact tuyệt đối khi chưa có link job verify.

### Theo độ phức tạp
| Loại task | Thời gian ước tính | Range giá (VND) |
|-----------|-------------------|-----------------|
| Script đơn giản (1-2 giờ) | 1-2 giờ | 300k - 800k |
| Medium automation (1 ngày) | 4-8 giờ | 1.5m - 3m |
| Complex + maintain | 1-2 tuần | 5m - 15m |
| Retainer (tuần/tháng) | 2-5 giờ/tuần | 2m - 5m/tháng |

### Theo platform
- **Local (Facebook, word-of-mouth)**: Thấp hơn, nhưng dễ deal.
- **Upwork/Fiverr**: $50-$200 cho small script, nhưng cạnh tranh cao.
- **TopCV/VietnamWorks**: Lương cứng 8m-15m/tháng cho intern/junior.

### Tips deal giá
- Luôn hỏi rõ scope trước khi báo giá.
- Báo giá theo deliverable, không theo giờ.
- Có option "basic" và "premium" (có maintain, có documentation).

---

## 5. Best Practices (Grounded in Reality)

### Code Quality
- Use `venv` cho mọi project.
- Viết `requirements.txt` (không ghi version quá cụ thể trừ khi cần).
- Thêm `README.md` với:
  - Cách cài đặt
  - Cách chạy
  - Sample input/output
- Comment chỉ ở chỗ logic phức tạp.

### Deliverables cho Freelance
- Script chính + `requirements.txt` + `README.md`.
- Sample input data + expected output.
- Video demo (Loom, 2-5 phút) showing how to run.
- Optional: `.env.example` nếu có API keys.

### Testing
- Test với sample data trước khi giao.
- Ghi lại edge cases đã xử lý.
- Nếu có lỗi, log rõ ràng (không chỉ `print()`).

### Security
- Không commit API keys lên GitHub.
- Dùng `.env` + `python-dotenv`.
- Không dùng script có risk spam/abuse (mass messaging, bot tự động like/follow).

---

## 6. Verification Log

- [x] Freelancer job links (7 links verified)
- [ ] TopCV/VietnamWorks links (cần verify còn active không)
- [ ] GitHub repos (5 repos verified, cần thêm 2-3 nữa)
- [ ] Case studies with screenshots (optional, có thể thêm sau)
- [ ] Pricing survey từ 3-5 freelance VN (cần research thêm)

---

## 7. Lesson Mapping

### Bài 1-6 (Fundamentals)
- Chưa kiếm tiền được.
- Nhấn mạnh: đây là nền tảng để ghép thành script sau này.

### Bài 7-15 (Data Structures, Functions)
- Có thể làm script nhỏ:
  - Clean CSV
  - Rename files
  - Simple calculator

### Bài 16-25 (File I/O, Modules)
- Có thể làm:
  - Merge Excel files
  - Generate reports
  - Simple web scraper

### Bài 26-35 (Advanced, APIs)
- Có thể làm:
  - Price monitoring bot
  - API integration (Google Sheets → Slack)
  - Automated email reporter

---

**Note cho coach:**
- Luôn gắn lesson với use-case thực tế.
- Nếu lesson chưa đủ để kiếm tiền, nói thẳng.
- Không bịa link job/repo. Nếu không verify được, bỏ.
- Ưu tiên case VN trước global.
