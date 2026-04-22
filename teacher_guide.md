# Teacher Guide: Data Pipeline & Semantic Observability

## 1. Mục tiêu bài học (Learning Objectives)
*   Hiểu tầm quan trọng của việc chuẩn hóa dữ liệu (Normalization) trước khi nạp vào AI Models.
*   Thực hành kỹ thuật **Schema Harmonization** để giải quyết xung đột dữ liệu từ nhiều nguồn.
*   Xây dựng tư duy **Observability**: Không chỉ quan tâm hệ thống "chạy được", mà phải quan tâm dữ liệu có "tin cậy được" không.

---

## 2. Hướng dẫn thiết lập GitHub Classroom
Để triển khai bài lab này trên GitHub Classroom, giảng viên thực hiện các bước sau:
1. Tạo một **Assignment** mới trên GitHub Classroom của lớp học.
2. Tại mục **Starter code**, chọn repository của bài lab này làm template.
3. Cấu hình **Autograding** (Tự động chấm điểm) theo 4 tiêu chí (Criteria). Khuyến nghị chia thành nhiều test cases (Chọn **Add test** -> **Run command**) với chi tiết như sau:
   - **Cài đặt chung cho tất cả các bài test:**
     - Setup command: `pip install pytest pydantic` (để cài đặt các thư viện cần thiết).
   - **Bài Test 1: EXECUTION (40 Điểm)**
     - Name: `Criteria 1: Execution`
     - Run command: `pytest tests/test_lab.py -k "test_execution"`
     - Points: 40
   - **Bài Test 2: OBSERVABILITY (20 Điểm)**
     - Name: `Criteria 2: Observability`
     - Run command: `pytest tests/test_lab.py -k "test_observability"`
     - Points: 20
   - **Bài Test 3: HARMONIZATION (30 Điểm)**
     - Name: `Criteria 3: Harmonization`
     - Run command: `pytest tests/test_lab.py -k "test_harmonization"`
     - Points: 30
   - **Bài Test 4: FINAL RESULT (10 Điểm)**
     - Name: `Criteria 4: Final Result`
     - Run command: `pytest tests/test_lab.py -k "test_final_output"`
     - Points: 10
4. Lưu cấu hình và chia sẻ **Invitation link** cho học viên.

---

## 3. Cấu trúc bài Lab
Bài lab được thiết kế theo mô hình **Collaborative Engineering**:
*   **Conflict Point**: Dữ liệu PDF dùng `docId`, dữ liệu Video dùng `video_id`. Nhiệm vụ của học viên là phải thống nhất về một key duy nhất là `document_id`.
*   **The Trap (Cái bẫy)**: File `raw_data/group_a_pdfs/doc2_corrupt.json` chứa nội dung là một lỗi hệ thống "Null pointer exception". Nếu học viên không viết Quality Gate, dữ liệu rác này sẽ đi thẳng vào AI Agent, gây ra lỗi suy luận sau này.

---

## 4. Hướng dẫn giảng dạy & Gợi ý (Tips)
*   **Giai đoạn 1 (Thiết kế)**: Khuyến khích Architect của các nhóm thảo luận với nhau. Nếu Architect định nghĩa sai Schema, toàn bộ Team sẽ không thể pass được phần test `Harmonization`.
*   **Giai đoạn 2 (Xử lý)**: Builder thường quên làm sạch text. Hãy nhắc học viên mở file `doc1_messy.json` để thấy các đoạn `HEADER_PAGE_1` làm nhiễu dữ liệu như thế nào.
*   **Giai đoạn 3 (Vận hành)**: Nhắc nhở về lỗi đường dẫn trên Windows. Code mẫu đã sử dụng `os.path.join` để hạn chế lỗi này, học viên nên tuân thủ theo.

---

## 5. Giải đáp và Chấm điểm (Grading)
Hệ thống chấm điểm tự động thông qua `pytest tests/test_lab.py`. 

**Bảng đáp án (Key Logic):**
1.  **Regex**: `re.sub(r'HEADER_PAGE_\d+|FOOTER_PAGE_\d+', '', text)`
2.  **Quality Check**: Cần sử dụng `.lower()` khi kiểm tra toxic keywords để tránh sót lỗi (ví dụ: "null pointer" vs "Null Pointer").
3.  **Orchestrator**: Cần xử lý cả 2 thư mục con trong `raw_data`.

---

## 6. Câu hỏi thảo luận mở rộng
1.  Nếu có 1.000.000 file PDF, cấu trúc vòng lặp hiện tại có vấn đề gì không? (Gợi ý: Cần xử lý song song/Batch processing).
2.  Làm thế nào để tự động hóa việc phát hiện "dữ liệu rác" mà không cần viết các từ khóa thủ công? (Gợi ý: Dùng LLM để chấm điểm chất lượng - LLM-as-a-judge).
