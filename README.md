# Simulated IoT Infrastructure

This project simulates a basic IoT infrastructure using Docker, Kubernetes, and Terraform. It integrates tools like Prometheus, Grafana, and InfluxDB to collect, store, and visualize sensor data.

## Table of Contents
- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [How to Use](#how-to-use)
- [Project Features](#project-features)
- [Future Enhancements](#future-enhancements)

## Overview
The project simulates a scalable IoT infrastructure for collecting, storing, and analyzing sensor data. It uses Docker for containerization and integrates key tools for monitoring and visualization:

- **Prometheus**: Metrics monitoring and alerting.
- **Grafana**: Visualization of metrics and sensor data.
- **InfluxDB**: Time-series database for storing sensor data.

## Technologies Used
- **Docker**: For containerization.
- **Prometheus**: Metrics collection.
- **Grafana**: Data visualization.
- **InfluxDB**: Time-series database.
- **Flask**: Backend API for the Data Collector.
- **Python**: For sensor simulation and backend logic.

## Architecture
The infrastructure includes the following components:

1. **Sensor Simulator**:
   - Simulates temperature and humidity data.
   - Sends data to the Data Collector service.

2. **Data Collector**:
   - Receives data from the Sensor Simulator.
   - Stores data in InfluxDB.
   - Exposes `/metrics` for Prometheus to scrape.

3. **Prometheus**:
   - Monitors the health of services.
   - Scrapes metrics from the Data Collector.

4. **Grafana**:
   - Visualizes sensor data and Prometheus metrics.

5. **InfluxDB**:
   - Stores time-series data (e.g., sensor readings).

### Architecture Diagram
![Architecture Diagram](path/to/diagram.png) <!-- Add a path or link to your diagram -->

## Setup Instructions
### Prerequisites
- Docker and Docker Compose installed.
- A modern browser for accessing Grafana and Prometheus UIs.

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/simulated_iot_infrastructure.git
   cd simulated_iot_infrastructure
2. Start the services:
   ```bash
   docker-compose up -d
3. Access the following:
   Prometheus: http://localhost:9090
   Grafana: http://localhost:3100
   InfluxDB: http://localhost:8086

## How to Use
### Simulate Sensor Data
1. The Sensor Simulator generates temperature and humidity readings every 5 seconds.
2. Data is sent to the Data Collector and stored in InfluxDB.

### Visualize Data
1. Open Grafana and add a data source for InfluxDB.
2. Create dashboards to visualize temperature and humidity trends.

### Monitor Metrics
1. Open Prometheus and query metrics such as `requests_total`.
2. View target health under **Status > Targets**.

## Project Features
- Simulated IoT data with realistic temperature and humidity readings.
- Scalable architecture using Docker.
- Centralized monitoring with Prometheus.
- Custom dashboards with Grafana.
- Persistent time-series data storage in InfluxDB.

## Future Enhancements
- Integrate Kubernetes for orchestration.
- Add Terraform for infrastructure as code (IaC).
- Expand to support multiple sensor types (e.g., motion, light).
- Implement alerting via Prometheus and Grafana.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)