import pytest
from fastapi.testclient import TestClient
from main import app
import json

# Create test client
client = TestClient(app)

# Get initial data for testing
response = client.get("/api/cars")
cars = response.json()
response = client.get("/api/users")
users = response.json()
response = client.get("/api/bookings")
bookings = response.json()
response = client.get("/api/events")
events = response.json()
response = client.get("/api/mapview")
map_views = response.json()

def test_get_cars():
    response = client.get("/api/cars")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "type" in data[0]

def test_get_users():
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]

def test_get_bookings():
    response = client.get("/api/bookings")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "car_id" in data[0]

def test_forecast_demand():
    # Test with existing area
    area_id = map_views[0].area_id
    response = client.get(f"/api/ai/forecast-demand/{area_id}")
    assert response.status_code == 200
    data = response.json()
    assert "expected_demand" in data
    assert "peak_dates" in data
    assert 0 <= data["expected_demand"] <= 1.0
    
    # Test with non-existing area
    response = client.get("/api/ai/forecast-demand/999")
    assert response.status_code == 404

def test_recommend_price():
    # Test with existing car
    car_id = cars[0].id
    response = client.get(f"/api/ai/recommend-price/{car_id}")
    assert response.status_code == 200
    data = response.json()
    assert "recommended_price" in data
    assert "reason" in data
    
    # Test with non-existing car
    response = client.get("/api/ai/recommend-price/999")
    assert response.status_code == 404

def test_map_insights():
    # Test with existing area
    area_id = map_views[0].area_id
    response = client.get(f"/api/ai/map-insights/{area_id}")
    assert response.status_code == 200
    data = response.json()
    assert "total_cars" in data
    assert "available_cars" in data
    assert "utilization_rate" in data
    
    # Test with non-existing area
    response = client.get("/api/ai/map-insights/999")
    assert response.status_code == 404

def test_can_cancel():
    # Test with existing booking
    booking_id = bookings[0].id
    response = client.get(f"/api/ai/can-cancel/{booking_id}")
    assert response.status_code == 200
    data = response.json()
    assert "can_cancel" in data
    assert "reason" in data
    
    # Test with non-existing booking
    response = client.get("/api/ai/can-cancel/999")
    assert response.status_code == 404

def test_recommend_cars():
    # Test with existing user
    user_id = users[0].id
    response = client.get(f"/api/ai/recommend-cars/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "recommended_cars" in data
    
    # Test with non-existing user
    response = client.get("/api/ai/recommend-cars/999")
    assert response.status_code == 404

def test_recommend_areas():
    # Test with existing user
    user_id = users[0].id
    response = client.get(f"/api/ai/recommend-areas/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert "user_id" in data
    assert "recommended_areas" in data
    
    # Test with non-existing user
    response = client.get("/api/ai/recommend-areas/999")
    assert response.status_code == 404

def test_hotspot_prediction():
    response = client.get("/api/ai/hotspot-prediction")
    assert response.status_code == 200
    data = response.json()
    assert "hotspots" in data
    assert "timestamp" in data
    assert isinstance(data["hotspots"], list)
    if len(data["hotspots"]) > 0:
        assert "area_id" in data["hotspots"][0]
        assert "expected_demand" in data["hotspots"][0]

if __name__ == "__main__":
    pytest.main(["-v", "test_api.py"])
