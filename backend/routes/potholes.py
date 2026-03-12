from fastapi import APIRouter

router = APIRouter()

@router.get("/potholes-test")

def test_potholes():

    return {

        "status":"potholes route working"

    }