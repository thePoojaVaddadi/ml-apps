from app import app

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_health():
    client = app.test_client()
    res = client.get("/health")
    assert res.status_code == 200

def test_predict():
    client = app.test_client()

    res = client.post("/predict", json={
        "size": 1200,
        "bedrooms": 2,
        "age": 5
    })

    assert res.status_code == 200