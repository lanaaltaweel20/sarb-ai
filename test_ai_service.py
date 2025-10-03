import requests
import json

def test_ai_service():
    """Test the AI service for booking cancellation"""
    # First get available bookings
    bookings_url = "http://localhost:8000/api/bookings"
    
    try:
        response = requests.get(bookings_url)
        response.raise_for_status()
        bookings = response.json()
        
        if bookings:
            # Test with the first booking
            booking_id = bookings[0]['id']
            ai_url = f"http://localhost:8000/api/ai/can-cancel/{booking_id}"
            
            ai_response = requests.get(ai_url)
            ai_response.raise_for_status()
            ai_data = ai_response.json()
            
            print(f"AI Service Test Results for Booking ID {booking_id}:")
            print(json.dumps(ai_data, indent=2))
        else:
            print("No bookings available for testing")
            
    except requests.exceptions.RequestException as e:
        print(f"Error testing AI service: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")

if __name__ == "__main__":
    test_ai_service()