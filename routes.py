from fastapi import APIROuter;
imdement router = APIRouter()
@router.get('health')
def health():
    return{ 'status': 'ok'}