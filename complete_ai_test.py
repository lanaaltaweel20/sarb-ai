import requests
import json

def test_all_ai_services():
    """Comprehensive test of all AI services"""
    
    base_url = "http://localhost:8000"
    
    print("=== Comprehensive AI Services Test ===")
    
    # Test existing AI services
    print("\n1. Testing Existing AI Services...")
    
    # Test demand forecast
    try:
        response = requests.get(f"{base_url}/api/ai/forecast-demand/1")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Demand Forecast for Area 1:")
        print(f"  Expected Demand: {result['expected_demand']}")
        print(f"  Peak Dates: {len(result['peak_dates'])} dates identified")
    except Exception as e:
        print(f"✗ Demand Forecast Error: {e}")
    
    # Test price recommendation
    try:
        response = requests.get(f"{base_url}/api/ai/recommend-price/38")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Price Recommendation for Car 38:")
        print(f"  Current Price: {result['current_price']}")
        print(f"  Recommended Price: {result['recommended_price']}")
    except Exception as e:
        print(f"✗ Price Recommendation Error: {e}")
    
    # Test cancellation policy
    try:
        response = requests.get(f"{base_url}/api/ai/can-cancel/52")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Cancellation Policy for Booking 52:")
        print(f"  Can Cancel: {result['can_cancel']}")
        print(f"  Reason: {result['reason']}")
    except Exception as e:
        print(f"✗ Cancellation Policy Error: {e}")
    
    # Test new AI services
    print("\n2. Testing New AI Services...")
    
    # Test Algorithm 1: Initial pricing recommendation
    try:
        response = requests.get(f"{base_url}/api/ai/recommend-initial-price?car_type=Sedan&location=Riyadh")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Initial Pricing Recommendation (Algorithm 1):")
        print(f"  Car Type: {result['car_type']}")
        print(f"  Location: {result['location']}")
        print(f"  Market Average: {result['market_average_price']}")
        print(f"  Recommended Price: {result['recommended_initial_price']}")
    except Exception as e:
        print(f"✗ Initial Pricing Recommendation Error: {e}")
    
    # Test AI Notifications for hosts
    try:
        response = requests.get(f"{base_url}/api/ai/host-notifications/15")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Host Notifications (AI Notifications) for Host 15:")
        print(f"  Total Cars: {result['total_cars']}")
        print(f"  Demand Notifications: {len(result['demand_notifications'])}")
        print(f"  Seasonal Notifications: {len(result['seasonal_notifications'])}")
    except Exception as e:
        print(f"✗ Host Notifications Error: {e}")
    
    # Test hotspot prediction
    try:
        response = requests.get(f"{base_url}/api/ai/hotspot-prediction")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Hotspot Prediction:")
        print(f"  Hotspots Identified: {len(result['hotspots'])}")
        if result['hotspots']:
            hotspot = result['hotspots'][0]
            print(f"  Top Hotspot - Area {hotspot['area_id']}: Expected Demand {hotspot['expected_demand']}")
    except Exception as e:
        print(f"✗ Hotspot Prediction Error: {e}")
    
    print("\n=== All AI Services Test Complete ===")

if __name__ == "__main__":
    test_all_ai_services()