from fastapi import APIRouter


api_bp = APIRouter()


@api_bp.post(path="/")
def dashboard():
    pass
