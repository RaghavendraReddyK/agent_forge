from fastapi import APIRouter

router = APIRouter(prefix="", tags=["Health_Check"])

@router.get("/health")
def health():
    return {"run": "success"}