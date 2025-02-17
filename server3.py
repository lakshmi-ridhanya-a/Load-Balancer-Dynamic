from flask import Flask, jsonify,request
import random
import time
import threading

app = Flask(__name__)

# Track active connections
active_connections = 0  # Tracks active connections

# Lock for thread safety
connection_lock = threading.Lock()

@app.route('/', methods=['GET', 'POST'])
def server_status():
    print("Received request on server with method:", request.method)
    global active_connections

    # Simulate request processing time
    processing_time = random.uniform(0.1, 2.0)  # Simulate processing time between 0.1 to 2.0 seconds

    # Increase active connections when a new request is received
    with connection_lock:
        active_connections += 1

    # Simulate processing by making the thread sleep
    time.sleep(processing_time)

    # Generate new random values for CPU and Memory load
    cpu_load = random.randint(10, 90)
    memory_load = random.randint(10, 90)

    # Decrease active connections after processing
    with connection_lock:
        active_connections -= 1

    # Return server metrics as JSON
    return jsonify({
        "cpu": cpu_load,
        "memory": memory_load,
        "connections": active_connections
    })

if __name__ == '__main__':
    # Change the port for each server instance
    app.run(port=5002)  # This will run on port 5000
