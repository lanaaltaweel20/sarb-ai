import requests
import json

def test_market_prices_api_integration():
    """Test that we can fetch market prices from the external API and transform them correctly"""
    # Test the local API endpoint
    response = requests.get("http://localhost:8000/api/market/average-prices")
    
    if response.status_code == 200:
        prices = response.json()
        print(f"Successfully fetched {len(prices)} market price entries from external API")
        
        # Check the structure of the first price entry
        if prices:
            price_entry = prices[0]
            required_fields = ["car_type", "average_price"]
            missing_fields = [field for field in required_fields if field not in price_entry]
            
            if not missing_fields:
                print("✅ Market price data structure is correct")
                print(f"Sample price entry: {price_entry}")
            else:
                print(f"❌ Missing fields in price entry: {missing_fields}")
        else:
            print("⚠️  No price entries returned from API")
    else:
        print(f"❌ Failed to fetch market prices. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_market_prices_api_integration()