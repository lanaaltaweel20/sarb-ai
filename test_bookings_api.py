import requests
import json

def test_bookings_api():
    """Test the bookings API endpoint"""
    url = "http://localhost:8000/api/bookings"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("Bookings API Test Results:")
        print(f"Status Code: {response.status_code}")
        print(f"Number of bookings: {len(data)}")
        
        if data:
            print("\nFirst booking:")
            print(json.dumps(data[0], indent=2))
        else:
            print("No bookings found")
            
    except requests.exceptions.RequestException as e:
        print(f"Error testing bookings API: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    test_bookings_api()