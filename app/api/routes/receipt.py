from fastapi import APIRouter, UploadFile, File

from app.services.ocr_service import OCRService
from app.domain.receipt_parser import ReceiptParser
from app.domain.macro_engine import MacroEngine

router = APIRouter()


@router.post("/parse-receipt")
async def parse_receipt(
    file: UploadFile = File(...)
):

    image = await file.read()

    ocr = OCRService()

    raw_text = await ocr.extract_text(
        image
    )

    parser = ReceiptParser()

    items = parser.extract_items(
        raw_text
    )

    engine = MacroEngine()

    result = engine.calculate(
        items
    )

    return result
