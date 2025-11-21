import requests
import json

def test_ai_services():
    base_url = "http://localhost:8001"
    
    print("Testing AI Services...")
    
    # Test Algorithm 2: Price recommendation
    print("\n1. Testing Price Recommendation (Algorithm 2)...")
    try:
        response = requests.get(f"{base_url}/api/ai/recommend-price/40")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Price Recommendation for Car ID 40:")
        print(f"  Car ID: {result['car_id']}")
        print(f"  Current Price: {result['current_price']}")
        print(f"  Recommended Price: {result['recommended_price']}")
        print(f"  Reason: {result['reason']}")
    except Exception as e:
        print(f"✗ Price Recommendation Error: {e}")
    
    # Test Algorithm 1: Initial pricing recommendation
    print("\n2. Testing Initial Pricing Recommendation (Algorithm 1)...")
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
    
    # Test Cancellation Policy
    print("\n3. Testing Cancellation Policy...")
    try:
        response = requests.get(f"{base_url}/api/ai/can-cancel/40")
        response.raise_for_status()
        result = response.json()
        print(f"✓ Cancellation Policy for Booking 40:")
        print(f"  Can Cancel: {result['can_cancel']}")
        print(f"  Reason: {result['reason']}")
    except Exception as e:
        print(f"✗ Cancellation Policy Error: {e}")
    
    print("\n=== AI Services Test Complete ===")

if __name__ == "__main__":
    test_ai_services()