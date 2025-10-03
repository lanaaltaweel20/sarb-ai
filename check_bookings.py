import requests
import json

def check_bookings():
    """Check available bookings"""
    url = "http://localhost:8000/api/bookings"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        print("Available bookings:")
        for booking in data:
            print(f"ID: {booking['id']}, Start: {booking['start_date']}, End: {booking['end_date']}")
            
    except requests.exceptions.RequestException as e:
        print(f"Error checking bookings: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    check_bookings()