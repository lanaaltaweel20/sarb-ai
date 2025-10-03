import requests
import json

def test_all_apis():
    """Comprehensive test of all API integrations"""
    
    base_url = "http://localhost:8000"
    
    # Test cars API
    print("Testing Cars API...")
    try:
        response = requests.get(f"{base_url}/api/cars")
        response.raise_for_status()
        cars = response.json()
        print(f"✓ Cars API: {len(cars)} cars retrieved")
    except Exception as e:
        print(f"✗ Cars API Error: {e}")
    
    # Test users API
    print("\nTesting Users API...")
    try:
        response = requests.get(f"{base_url}/api/users")
        response.raise_for_status()
        users = response.json()
        print(f"✓ Users API: {len(users)} users retrieved")
    except Exception as e:
        print(f"✗ Users API Error: {e}")
    
    # Test bookings API
    print("\nTesting Bookings API...")
    bookings = []  # Initialize to avoid linter error
    try:
        response = requests.get(f"{base_url}/api/bookings")
        response.raise_for_status()
        bookings = response.json()
        print(f"✓ Bookings API: {len(bookings)} bookings retrieved")
    except Exception as e:
        print(f"✗ Bookings API Error: {e}")
    
    # Test market prices API
    print("\nTesting Market Prices API...")
    try:
        response = requests.get(f"{base_url}/api/market/average-prices")
        response.raise_for_status()
        prices = response.json()
        print(f"✓ Market Prices API: {len(prices)} price entries retrieved")
    except Exception as e:
        print(f"✗ Market Prices API Error: {e}")
    
    # Test AI services if we have data
    if bookings:
        print("\nTesting AI Services...")
        try:
            # Test can-cancel service
            booking_id = bookings[0]['id']
            response = requests.get(f"{base_url}/api/ai/can-cancel/{booking_id}")
            response.raise_for_status()
            result = response.json()
            print(f"✓ AI Can-Cancel Service: Booking {booking_id} - {result['reason']}")
        except Exception as e:
            print(f"✗ AI Can-Cancel Service Error: {e}")
        
        try:
            # Test price recommendation service
            car_id = bookings[0]['car_id']
            response = requests.get(f"{base_url}/api/ai/recommend-price/{car_id}")
            response.raise_for_status()
            result = response.json()
            print(f"✓ AI Price Recommendation Service: Car {car_id} - Current: {result['current_price']}, Recommended: {result['recommended_price']}")
        except Exception as e:
            print(f"✗ AI Price Recommendation Service Error: {e}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    test_all_apis()