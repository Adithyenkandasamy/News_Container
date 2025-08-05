from fastapi import APIRouter, Query
from typing import Optional
from services.news_fetch import get_top_news

router = APIRouter()

@router.get("/news")
def get_news(
    category: Optional[str] = Query(
        "general",
        description="News category",
        enum=["general", "business", "entertainment", "health", "science", "sports", "technology"]
    ),
    country: Optional[str] = Query(
        "in",
        description="2-letter country code",
        enum=["in", "us", "gb", "au", "ca"]
    ),
    count: Optional[int] = Query(5, description="Number of articles to fetch (1-20)", ge=1, le=20)
):
    news = get_top_news(country=country, category=category, count=count)
    return {"articles": news}
