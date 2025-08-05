from fastapi import APIRouter, Query
from services.youtube_fetch import search_youtube_videos

router = APIRouter()

@router.get("/search")
def search_videos(query: str = Query(..., description="Search term for YouTube")):
    videos = search_youtube_videos(query)
    return {"results": videos}
