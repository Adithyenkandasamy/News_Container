from fastapi import APIRouter, Request
from pydantic import BaseModel
from services.summary_ai import summarize_article

router = APIRouter()

class ArticleData(BaseModel):
    content: str

@router.post("/summarize")
def summarize(article: ArticleData):
    summary = summarize_article(article.content)
    return {"summary": summary}
