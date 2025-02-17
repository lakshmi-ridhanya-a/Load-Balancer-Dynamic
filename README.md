# Dynamic Load Balancer for Flask Microservices

![Python](https://img.shields.io/badge/python-3.9%2B-blue) ![Flask](https://img.shields.io/badge/flask-2.0-green)

---

## Overview

A **Dynamic Load Balancer** built with Flask to distribute client requests across multiple backend servers using the **least loaded algorithm**. The system ensures optimal resource utilization by tracking **CPU usage**, **memory usage**, and **active connections** in real time. 

Key components:
- **Load Balancer**: Routes requests to the least loaded server and predicts load spikes.
- **Client Simulator**: Simulates realistic traffic with random requests.
- **Backend Servers**: Process requests and return load metrics for dynamic routing.

---

## Features

- **Dynamic Load Balancing**: Routes traffic to the server with minimal load.
- **Real-Time Monitoring**: Tracks CPU, memory, and active connections.
- **Scalability**: Easily add new servers for horizontal scaling.
- **Simulation Tools**: Generates traffic to evaluate performance and resilience.

---

## How It Works

1. **Load Balancer** queries backend servers for load metrics and predicts future load.
2. **Backend Servers** process requests and provide live CPU, memory, and connection data.
3. **Client Simulator** sends randomized **GET** and **POST** requests to stress test the system.

---

## Getting Started

### 1. Setup Environment
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
pip install -r requirements.txt
```

### 2. Start Backend Servers
Start each backend server in separate terminals:
```bash
python server1.py  # Starts on port 5000
python server2.py  # Starts on port 5001
```
Repeat for additional servers.

### 3. Run Load Balancer
Launch the load balancer:
```bash
python load-balance.py
```
This starts the balancer on port `8000`.

### 4. Simulate Clients
Generate traffic using the client simulator:
```bash
python client-sim.py
```
Logs response times and server assignments.

---

## Project Structure

```
.
├── client-sim.py        # Client simulator
├── load-balance.py      # Load balancer
├── server1.py           # Backend server 1
├── server2.py           # Backend server 2
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```
