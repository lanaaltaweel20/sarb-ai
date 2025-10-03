import requests
import json

def test_new_ai_services():
    """Test the newly added AI services"""
    
    base_url = "http://localhost:8000"
    
    print("Testing New AI Services...")
    
    # Test Algorithm 1: Initial pricing recommendation
    print("\n1. Testing Initial Pricing Recommendation (Algorithm 1)...")
    try:
        response = requests.get(f"{base_url}/api/ai/recommend-initial-price?car_type=Sedan&location=Riyadh")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Initial Pricing Recommendation:")
        print(f"  Car Type: {result['car_type']}")
        print(f"  Location: {result['location']}")
        print(f"  Market Average: {result['market_average_price']}")
        print(f"  Recommended Price: {result['recommended_initial_price']}")
        print(f"  Reason: {result['reason']}")
    except Exception as e:
        print(f"✗ Initial Pricing Recommendation Error: {e}")
    
    # Test AI Notifications for hosts
    print("\n2. Testing Host Notifications (AI Notifications)...")
    try:
        # Use host_id 15 as it appears in the sample data
        response = requests.get(f"{base_url}/api/ai/host-notifications/15")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Host Notifications for Host ID {result['host_id']}:")
        print(f"  Total Cars: {result['total_cars']}")
        print(f"  Demand Notifications: {len(result['demand_notifications'])}")
        print(f"  Seasonal Notifications: {len(result['seasonal_notifications'])}")
        
        if result['demand_notifications']:
            print("  Sample Demand Notification:")
            notification = result['demand_notifications'][0]
            print(f"    Date: {notification['date']}")
            print(f"    Message: {notification['message']}")
        
        if result['seasonal_notifications']:
            print("  Sample Seasonal Notification:")
            notification = result['seasonal_notifications'][0]
            print(f"    Period: {notification['period']}")
            print(f"    Message: {notification['message']}")
    except Exception as e:
        print(f"✗ Host Notifications Error: {e}")
    
    print("\n=== New AI Services Test Complete ===")

if __name__ == "__main__":
    test_new_ai_services()