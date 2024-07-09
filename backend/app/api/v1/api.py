from fastapi import APIRouter


api_bp = APIRouter()


@api_bp.post(path="/dashboard", summary="仪表盘")
def dashboard():
    pass


@api_bp.post(path="/vulns", summary="漏洞列表")
def vulns():
    pass

