from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn. 
    TODO: Điền kiểu dữ liệu (str) cho các trường còn thiếu bên dưới.
    """
    document_id: str
    source_type: str 
    author: str
    category: str
    content: str
    timestamp: str
