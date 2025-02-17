# client-sim.py
import asyncio
import aiohttp
import random
import time

# URL of the load balancer
LOAD_BALANCER_URL = "http://127.0.0.1:8000/route"

# Simulating different types of client requests
REQUEST_TYPES = ["GET", "POST"]

# Function to simulate a client sending a request with varied load
async def simulate_client(client_id, session):#c
    try:
        while True:  # Loop to continuously send requests
            # Randomly choose request type
            request_type = random.choice(REQUEST_TYPES)
            payload = {"data": random.randint(1, 100)} if request_type == "POST" else None #payload: dictionary containing single key-value pair where sata is integer from 1 - 100
            headers = {"Content-Type": "application/json"} if request_type == "POST" else {}

            print(f"Client {client_id} is sending a {request_type} request...")

            # Record the start time
            start_time = time.time()

            if request_type == "GET":
                async with session.get(LOAD_BALANCER_URL) as response:
                    response_data = await response.json()
                    status = response.status#captures http sttaus codes
                    server = response_data.get('server', 'Unknown server')  # Extract the server from the response
                    print(f"Client {client_id} received response: {response_data} (Status: {status}, Time: {time.time() - start_time:.2f} seconds, Server: {server})")
                    
            elif request_type == "POST":
                async with session.post(LOAD_BALANCER_URL, json=payload, headers=headers) as response:
                    response_data = await response.json()
                    status = response.status
                    server = response_data.get('server', 'Unknown server')  # Extract the server from the response
                    print(f"Client {client_id} received response: {response_data} (Status: {status}, Time: {time.time() - start_time:.2f} seconds, Server: {server})")

            # Introduce a random delay between requests to simulate real behavior
            await asyncio.sleep(random.uniform(1, 3))

    except Exception as e:
        print(f"Client {client_id} encountered an error: {str(e)}")

# Function to continuously simulate new clients
async def simulate_clients():
    async with aiohttp.ClientSession() as session:#maintain a persistent hhtpp session
        client_id = 0
        while True:  # Infinite loop to keep creating new clients
            task = asyncio.create_task(simulate_client(client_id, session))
            client_id += 1  # Increment client ID for the next client
            await asyncio.sleep(1)  # Delay before adding a new client

# Run the client simulator
if __name__ == "__main__":
    try:
        # Simulate clients asynchronously
        asyncio.run(simulate_clients())
    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
