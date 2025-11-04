"""
Simple example client to send JSON data to the medichek-server.
Run the server first with: python manage.py runserver
Then run this script: python example_client.py
"""

import requests
import json

BASE_URL = "http://localhost:8000/api"

def send_data():
    """Send JSON data to the server."""
    print("=== Sending JSON Data to Server ===\n")
    
    # Example data to send
    data = {
        "patient_id": "patient-123",
        "medication": "aspirin",
        "dosage": "100mg",
        "timestamp": "2025-11-04T12:00:00Z",
        "notes": "Patient responding well"
    }
    
    print(f"Data to send:\n{json.dumps(data, indent=2)}\n")
    
    try:
        response = requests.post(
            f"{BASE_URL}/data/",
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        print(f"Server Response:\n{json.dumps(response.json(), indent=2)}")
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")
        print("Make sure the server is running: python manage.py runserver")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    send_data()
