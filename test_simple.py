from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "SARB AI API" in response.text

def test_get_cars():
    response = client.get("/api/cars")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "type" in data[0]

if __name__ == "__main__":
    test_read_main()
    test_get_cars()
    print("Basic tests completed successfully!")
