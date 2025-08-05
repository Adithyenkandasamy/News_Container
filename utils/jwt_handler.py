import jwt
from datetime import datetime, timedelta

SECRET_KEY = "your_secret_key"

def create_jwt_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(days=1)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
