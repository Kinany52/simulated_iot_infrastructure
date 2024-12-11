import time
import random
import requests

# URLs
COLLECTOR_URL = "http://data_collector:5000/data"
HEALTH_URL = "http://data_collector:5000/health"

# Retry logic to wait for the Data Collector to become available
max_retries = 12  # Retry for up to 1 minute
retries = 0

while retries < max_retries:
    try:
        response = requests.get(HEALTH_URL)
        if response.status_code == 200:
            print("Data Collector is ready. Starting data transmission...")
            break
    except requests.exceptions.ConnectionError:
        print(f"Attempt {retries + 1}/{max_retries}: Waiting for Data Collector...")
    time.sleep(5)
    retries += 1
else:
    print("Data Collector is not ready after multiple retries. Exiting...")
    exit(1)

def generate_sensor_data():
    """
    Simulates sensor data for temperature and humidity.
    """
    return {
        "temperature": random.uniform(20.0, 30.0),
        "humidity": random.uniform(40.0, 60.0)
    }

def send_data_to_collector(data):
    """
    Sends sensor data to the data collector API.
    """
    try:
        response = requests.post(COLLECTOR_URL, json=data)
        print(f"Sent: {data}, Response Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")

if __name__ == "__main__":
    print("Starting sensor simulator...")
    while True:
        sensor_data = generate_sensor_data()
        send_data_to_collector(sensor_data)
        time.sleep(5)  # Wait 5 seconds before sending the next batch