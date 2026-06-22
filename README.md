# autonomous-receipt-macro-parser
The project is an "Autonomous Receipt-to-Macro Parser" built using Python and FastAPI.

# Autonomous Receipt-to-Macro Parser

Production-grade FastAPI microservice that converts receipt images into structured nutrition macro calculations.

---

## Features

✓ Receipt ingestion

✓ OCR abstraction layer

✓ Macro extraction

✓ Nutrition matching

✓ Structured JSON output

✓ Stateless architecture

✓ Containerized deployment

---

## Architecture

Client
↓

FastAPI Endpoint

↓

OCR Layer

↓

Receipt Parser

↓

Item Matcher

↓

Macro Engine

↓

JSON Response

---

## Installation

git clone REPOSITORY

cd autonomous-receipt-macro-parser

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload

---

## Endpoint

POST

/api/v1/parse-receipt

---

## Request

multipart/form-data

file:
receipt.jpg

---

## Example Response

{
  "items":[
    {
      "item":"banana",
      "calories":105,
      "protein":1.3,
      "carbs":27,
      "fat":0.4
    },
    {
      "item":"rice",
      "calories":205,
      "protein":4,
      "carbs":45,
      "fat":0.4
    }
  ],

  "totals":{
    "calories":310,
    "protein":5.3,
    "carbs":72,
    "fat":0.8
  }
}

---

## Production Extensions

- Swap OCRService → Vision provider
- Replace nutrition_db → USDA
- Add Redis cache
- Add async queue
- Add multi-tenant auth
- Add OpenAPI SDK generation
