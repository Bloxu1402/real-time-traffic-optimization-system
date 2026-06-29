import time
import os

def read_live_traffic():
    """Reads the latest vehicle count written by the CV script."""
    if os.path.exists("live_traffic_data.txt"):
        with open("live_traffic_data.txt", "r") as f:
            try:
                return int(f.read().strip())
            except ValueError:
                return 0
    return 0

def calculate_dynamic_green_time(vehicle_count):
    """
    Traffic Optimization Algorithm:
    Base green light is 10 seconds. Each car adds 2.5 additional seconds.
    Min limit = 10s, Max limit = 45s (to avoid starving other lanes).
    """
    base_time = 10
    additional_time = vehicle_count * 2.5
    calculated_time = base_time + additional_time
    
    # Clamp values between strict bounds
    return int(max(10, min(calculated_time, 45)))

print("--- Dynamic Traffic Controller Active ---")

try:
    while True:
        # 1. Fetch current traffic density
        cars_waiting = read_live_traffic()
        
        # 2. Compute customized green light allocation
        green_duration = calculate_dynamic_green_time(cars_waiting)
        
        # 3. Output state commands (Simulating signaling the physical lights)
        print(f"\n[TRAFFIC STATE]: {cars_waiting} cars detected.")
        print(f"-> Action: Setting Light to GREEN for {green_duration} seconds.")
        
        # Simulate countdown timer for the green light cycle
        time.sleep(green_duration)
        
        print("-> Action: Transitioning to YELLOW for 3 seconds.")
        time.sleep(3)
        
        print("-> Action: Light is RED. Yielding to next intersection lane...")
        time.sleep(5) # Standard red phase delay

except KeyboardInterrupt:
    print("\nShutting down Traffic Controller System Safely.")
