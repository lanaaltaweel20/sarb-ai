import requests
import json

def test_user_api_integration():
    """Test that we can fetch users from the external API and transform them correctly"""
    # Test the local API endpoint
    response = requests.get("http://localhost:8000/api/users")
    
    if response.status_code == 200:
        users = response.json()
        print(f"Successfully fetched {len(users)} users from external API")
        
        # Check the structure of the first user
        if users:
            user = users[0]
            required_fields = ["id", "name"]
            missing_fields = [field for field in required_fields if field not in user]
            
            if not missing_fields:
                print("✅ User data structure is correct")
                print(f"Sample user: {user}")
                
                # Verify that fields not provided by external API are NOT present
                removed_fields = ["age", "location", "preferences", "history_of_bookings"]
                unexpected_fields = [field for field in removed_fields if field in user]
                
                if not unexpected_fields:
                    print("✅ Removed fields are not present in user data")
                else:
                    print(f"❌ Unexpected fields found: {unexpected_fields}")
            else:
                print(f"❌ Missing fields in user data: {missing_fields}")
        else:
            print("⚠️  No users returned from API")
    else:
        print(f"❌ Failed to fetch users. Status code: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    test_user_api_integration()