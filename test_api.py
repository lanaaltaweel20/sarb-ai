import requests
import time

# Give the server a moment to start
time.sleep(2)

try:
    # Test the price recommendation API
    response = requests.get('http://localhost:8001/api/ai/recommend-price/40', timeout=10)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")