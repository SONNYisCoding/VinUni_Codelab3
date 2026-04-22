from pydantic import BaseModel, Field
from typing import Optional

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT (SOLUTION)
# ==========================================

class UnifiedDocument(BaseModel):
    document_id: str = Field(..., description="Unique ID for the document")
    source_type: str = Field(..., description="E.g., PDF, Video")
    author: Optional[str] = Field(None, description="Creator or author name")
    category: Optional[str] = Field(None, description="Normalized category")
    content: str = Field(..., description="The main corpus text")
    timestamp: str = Field(..., description="ISO 8601 string representing creation time")
