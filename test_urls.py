import requests

# Test the new URLs to make sure they're correctly updated
def test_urls():
    headers = {
        "Authorization": "Bearer 55|IQaLyRxU3h7SAAqI6a52zdqKSDZ5WQHB9tKWKvKCbeb9fd6e"
    }
    
    urls = [
        "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car",
        "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/user",
        "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/car/average-price",
        "https://powderblue-jaguar-171084.hostingersite.com/public/api/v1/booking"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f"URL: {url}")
            print(f"Status Code: {response.status_code}")
            if response.status_code == 200:
                print("✅ Success")
            else:
                print("❌ Failed")
            print("-" * 50)
        except Exception as e:
            print(f"URL: {url}")
            print(f"Error: {e}")
            print("❌ Failed")
            print("-" * 50)

if __name__ == "__main__":
    test_urls()