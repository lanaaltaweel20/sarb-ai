import requests
import json

def test_external_api_integration():
    """Test that we can fetch cars from the external API and transform them correctly"""
    # Test the local API endpoint
    response = requests.get("http://localhost:8000/api/cars")
    
    if response.status_code == 200:
        cars = response.json()
        print(f"Successfully fetched {len(cars)} cars from external API")
        
        # Check the structure of the first car
        if cars:
            car = cars[0]
            required_fields = ["id", "type", "model", "year", "price_per_day", "location", "availability"]
            missing_fields = [field for field in required_fields if field not in car]
            
            if not missing_fields:
                print("✅ Car data structure is correct")
                print(f"Sample car: {car}")
                
                # Verify that rating field is NOT present (as requested)
                if "rating" not in car:
                    print("✅ Rating field successfully removed")
                else:
                    print("❌ Rating field still present")
            else:
                print(f"❌ Missing fields in car data: {missing_fields}")
        else:
            print("⚠️  No cars returned from API")
    else:
        print(f"❌ Failed to fetch cars. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_external_api_integration()