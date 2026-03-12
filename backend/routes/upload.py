from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Form

from utils.response import success
from utils.response import error

from services.integration_service import mock_ai_analysis
from services.integration_service import mock_s3_upload
from services.integration_service import build_incident_record

from config import settings


router = APIRouter()



@router.post("/upload")

async def upload_incident(

        image: UploadFile = File(...),

        latitude: float = Form(...),

        longitude: float = Form(...)

):

    try:

        # FILE TYPE VALIDATION

        if image.content_type not in settings.ALLOWED_TYPES:

            return error(
                "Invalid file type"
            )


        # AI ANALYSIS (mock)

        ai_result = mock_ai_analysis()


        # AWS UPLOAD (mock)

        s3_result = mock_s3_upload()


        # BUILD INCIDENT

        incident = build_incident_record(

            latitude,

            longitude,

            ai_result["severity"],

            s3_result["image_url"]

        )


        return success(

            incident,

            "incident recorded"

        )


    except Exception as e:

        return error(

            str(e)

        )