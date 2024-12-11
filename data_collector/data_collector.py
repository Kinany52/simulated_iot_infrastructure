from flask import Flask, request
from influxdb_client import InfluxDBClient, Point
from prometheus_client import start_http_server, Counter
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Prometheus Metrics
request_counter = Counter('requests_total', 'Total number of requests', ['method', 'endpoint'])

@app.before_request
def before_request():
    request_counter.labels(method=request.method, endpoint=request.path).inc()

# InfluxDB setup
influxdb_url = os.getenv("INFLUXDB_URL", "http://localhost:8086") # I think this is correct
token = os.getenv("INFLUXDB_TOKEN", "default_token")
org = os.getenv("INFLUXDB_ORG", "default_org")      # Organization name
bucket = os.getenv("INFLUXDB_BUCKET", "default_bucket")         # Bucket name

# Initialize InfluxDB client
client = InfluxDBClient(url=influxdb_url, token=token)

@app.route("/data", methods=["POST"])
def collect_data():
    """
    Endpoint to receive sensor data and store it in InfluxDB.
    """
    data = request.json
    print(f"Received data: {data}")

    # Write data to InfluxDB
    point = Point("sensor_data") \
        .field("temperature", data["temperature"]) \
        .field("humidity", data["humidity"])
    write_api = client.write_api()
    write_api.write(bucket, org, point)

    return "Data stored successfully", 200

@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return "OK", 200

if __name__ == "__main__":
    print("Starting Data Collector...")
     # Start Prometheus metrics server on port 8000
    start_http_server(8000)  
    app.run(host="0.0.0.0", port=5000)  # Flask app serves other endpoints on port 5000
