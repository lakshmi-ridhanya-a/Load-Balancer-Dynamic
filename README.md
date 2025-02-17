# Load-Balancer-Dynamic
# Dynamic Load Balancer for Flask Microservices

![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![Flask](https://img.shields.io/badge/flask-2.0-green)

---

## Introduction

This project implements a **Dynamic Load Balancer** using Flask to efficiently distribute incoming client requests across multiple backend servers. It employs a **least-loaded algorithm** to ensure optimal resource usage while monitoring **CPU utilization, memory consumption, and active connections** in real time.

### Key Components:
- **Load Balancer**: Directs traffic to the least burdened server and anticipates potential load spikes.
- **Client Traffic Generator**: Simulates varying loads to evaluate system performance.
- **Backend Servers**: Handle requests and relay real-time load metrics for intelligent routing.

---

## Features

✔ **Smart Load Distribution**: Redirects requests to the server with the lightest load.
✔ **Live Performance Tracking**: Monitors CPU, memory, and active connection statistics.
✔ **Easily Scalable**: Allows seamless addition of new servers.
✔ **Traffic Simulation**: Generates diverse client requests to test efficiency.

---

## How It Works

1. The **Load Balancer** periodically gathers performance metrics from each backend server.
2. **Backend Servers** process requests while reporting system statistics.
3. The **Client Simulator** initiates randomized **GET** and **POST** requests to create dynamic traffic.

---

## Getting Started

### 1. Environment Setup
Ensure Python 3.9+ is installed, then create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

### 2. Launch Backend Servers
Run each server on separate terminals:
```bash
python server1.py  # Runs on port 5000
python server2.py  # Runs on port 5001
```
Add more servers as needed.

### 3. Start Load Balancer
Execute the load balancer script:
```bash
python load-balance.py
```
The balancer listens on port `8000`.

### 4. Simulate Client Requests
Generate simulated client requests:
```bash
python client-sim.py
```
This logs response times and server assignments.

---

## Project Directory Structure

```
.
├── client-sim.py        # Simulates client traffic
├── load-balance.py      # Core load balancer logic
├── server1.py           # Backend server 1
├── server2.py           # Backend server 2
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

This setup ensures a dynamic and scalable microservice architecture capable of handling fluctuating loads efficiently.

