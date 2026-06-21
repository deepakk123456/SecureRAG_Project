# core/schemas.py (Add this at the bottom)
from pydantic import BaseModel
from typing import List

class ChatMessageNode(BaseModel):
    role: str # 'user' or 'assistant'
    content: str

class ConversationMemoryBuffer(BaseModel):
    history: List[ChatMessageNode] = []