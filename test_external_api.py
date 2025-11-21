import requests
import json

def test_external_apis():
    headers = {
        "Authorization": "Bearer 28|KKyjTwdNzLQBjb44Iw8ZCabGjr9zWVIiMfIXQVQS36aa992f"
    }
    
    # Test bookings API
    print("Testing Bookings API...")
    bookings_url = "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/booking"
    try:
        response = requests.get(bookings_url, headers=headers)
        print(f"Bookings API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Bookings data keys: {list(data.keys())}")
            sample_data = data.get("result", {}).get("data", [])
            if sample_data:
                print(f"Sample booking structure: {list(sample_data[0].keys())}")
                print(f"Sample booking: {sample_data[0]}")
            else:
                print("No booking data found")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Bookings API Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test cars API
    print("Testing Cars API...")
    cars_url = "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car"
    try:
        response = requests.get(cars_url, headers=headers)
        print(f"Cars API Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"Cars data keys: {list(data.keys())}")
            sample_data = data.get("result", {}).get("data", [])
            if sample_data:
                print(f"Sample car structure: {list(sample_data[0].keys())}")
            else:
                print("No car data found")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Cars API Error: {e}")

if __name__ == "__main__":
    test_external_apis()