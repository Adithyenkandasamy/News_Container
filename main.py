from fastapi import FastAPI
from routers import auth, articles, youtube

app = FastAPI()

# Include routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(articles.router, prefix="/articles", tags=["Articles"])
app.include_router(youtube.router, prefix="/youtube", tags=["YouTube"])

@app.get("/")
def read_root():
    return {"message": "AI Info Platform Backend"}
