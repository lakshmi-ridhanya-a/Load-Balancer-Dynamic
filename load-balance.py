# load-balance.py
from flask import Flask, jsonify, request#HTTP requests
import requests#backend servers
from collections import deque
import time 


app = Flask(__name__)#web application

# List of server URLs
servers = [#url of a backend server
    "http://127.0.0.1:5000",
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003",
]
# Tracking request distribution and load metrics
request_distribution = {server: [] for server in servers}#each server url maps to an empty lsit, storing timestamps
load_over_time = {server: {"cpu": [], "memory": []} for server in servers}#each servers cpu and memory usage overtime


# Dictionary to store load history for each server
load_history = {server: deque(maxlen=10) for server in servers}#recent load values 

# Function to get the load (CPU and memory) from a server
def get_server_load(server):
    try:
        response = requests.get(server)#sends a get req to the server url, for losd ( cpu and memory usage )
        response.raise_for_status()  # Raises an error for HTTP error responses
        load = response.json()#contains cpu and memory usage  
        
        # Correct the total load calculation: Calculate average of CPU and memory load
        # total_load = (0.7 * load["cpu"]) + (0.3 * load["memory"])  # Fix precedence error

        #load_history[server].append(total_load)  # Update the load history
        return load
    except requests.RequestException as e:
        print(f"Error contacting server {server}: {e}")
        return None

# Function to find the server with the least predicted load
def find_least_loaded_server():
    least_loaded_server = None
    lowest_predicted_load = float('inf')  # Initialize with infinity
    load_spike_threshold = 70#identify spikes 

    for server in servers:
        load = get_server_load(server)
        if load:
            cpu_load = load["cpu"]
            memory_load = load["memory"]
            total_load = (cpu_load + memory_load) / 2

            load_over_time[server]["cpu"].append(cpu_load)
            load_over_time[server]["memory"].append(memory_load)
            # load_history[server].append(total_load)

            # Calculate historical average load for the server
            historical_average = sum(load_history[server]) / len(load_history[server]) if load_history[server] else total_load

            # Predict the load considering recent history
            if historical_average > load_spike_threshold:
                print(f"Warning: Predicted load spike on {server} based on recent history")
                predicted_load = historical_average
            else:
                predicted_load = total_load

            print(f"Server: {server}, Current Load: {total_load}, Predicted Load: {predicted_load}")

            # Find the server with the lowest predicted load
            if predicted_load < lowest_predicted_load:
                lowest_predicted_load = predicted_load
                least_loaded_server = server#current server becomes the least loaded server

    return least_loaded_server

@app.route('/route', methods=['GET', 'POST'])#maps http to route request
def route_request():
    least_loaded_server = find_least_loaded_server()
    if least_loaded_server:
        print(f"Routing request to: {least_loaded_server}")
        request_distribution[least_loaded_server].append(time.time())  # when req are routed to the server
        try:
            if request.method == 'POST':
                # Forward POST request, including headers and JSON payload
                response = requests.post(
                    least_loaded_server,
                    json=request.json,
                    headers={'Content-Type': request.headers.get('Content-Type')}
                )
            else:
                # Handle GET request
                response = requests.get(least_loaded_server)#forwards get requests to the least loaded server

            response.raise_for_status()  # Raises an error for HTTP error responses, if the respnse was successful
            response_data = response.json()
            response_data['server'] = least_loaded_server  # Add server info to response
            
            # Return the response including the server information
            return jsonify(response_data), response.status_code

        except requests.RequestException as e:#base class for all errors of requests
            print(f"Error during request forwarding: {e}")
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "No server available"}), 503

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
