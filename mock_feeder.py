import time
import random

print("--- Mock CV Traffic Feeder Active ---")
print("Simulating real-time car detections... Press Ctrl+C to stop.")

try:
    while True:
        # Simulate a random number of cars waiting at the light (0 to 20)
        simulated_cars = random.randint(0, 20)
        
        # Write directly to the file the controller is reading
        with open("live_traffic_data.txt", "w") as f:
            f.write(str(simulated_cars))
            
        print(f"[CV Feed]: Updating lane queue -> {simulated_cars} cars waiting.")
        
        # Update the traffic state every 8 seconds
        time.sleep(8)

except KeyboardInterrupt:
    print("\nStopping Mock Data Feed.")
