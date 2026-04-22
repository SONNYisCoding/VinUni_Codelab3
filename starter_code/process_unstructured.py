import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================

def process_pdf_data(raw_json: dict) -> dict:
    # Bước 1: Làm sạch nhiễu (Header/Footer) khỏi văn bản
    raw_text = raw_json.get("extractedText", "")
    # TODO: Dùng re.sub để xóa 'HEADER_PAGE_X' và 'FOOTER_PAGE_X'
    cleaned_content = re.sub(r'HEADER_PAGE_\d+|FOOTER_PAGE_\d+', '', raw_text)
    
    # Bước 2: Map dữ liệu thô sang định dạng chuẩn
    return {
        "document_id": raw_json.get("docId"),
        "source_type": "PDF",
        "author": raw_json.get("authorName", "Unknown"),
        "category": raw_json.get("docCategory"),
        "content": cleaned_content.strip(),
        "timestamp": raw_json.get("createdAt")
    }

def process_video_data(raw_json: dict) -> dict:
    # TODO: Điền các key tương ứng từ raw_json (video_id, creator_name, transcript...)
    return {
        "document_id": raw_json.get("video_id"),
        "source_type": "Video",
        "author": raw_json.get("creator_name", "Unknown"),
        "category": raw_json.get("category"),
        "content": raw_json.get("transcript"),
        "timestamp": raw_json.get("published_timestamp")
    }
