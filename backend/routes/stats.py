from fastapi import APIRouter

router = APIRouter()

@router.get("/stats-test")

def test_stats():

    return {

        "status":"stats route working"

    }