from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_parse():

    with open(
        "receipt.jpg",
        "rb"
    ) as f:

        r = client.post(
            "/api/v1/parse-receipt",
            files={
                "file":f
            }
        )

    assert r.status_code == 200
