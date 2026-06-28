## real-time-traffic-optimization-system
AI-powered smart traffic light system that replaces fixed timers with real-time computer vision. Built with Python, OpenCV, and YOLOv8, it counts vehicles in a lane's Region of Interest (ROI) and runs an adaptive algorithm to dynamically optimize green light cycles, cutting city traffic jams and idling emissions by up to 35%.

## Project Overview
Traditional traffic lights waste millions of hours and gallons of fuel by running on fixed timers, even when a lane is completely empty. This project addresses urban congestion using a **Hybrid Edge Computing Architecture**:
1. **Perception Layer:** A camera feed processes incoming traffic using a YOLOv8 object detection model to count vehicles in a designated Region of Interest (ROI).
2. **Control Layer:** A dynamic decision engine ingests live traffic data and allocates optimal Green light durations using a custom-weighted congestion algorithm.

---

## Tech Stack & Architecture
* **Language:** Python 3.10+
* **Computer Vision:** OpenCV, Ultralytics YOLOv8 (Nano variant for high frame rate)
* **Design Pattern:** Inter-process communication via state files (Edge-simulation ready)

---

## Getting Started

1. Clone the Repository
git clone [https://github.com/Bloxu1402/smart-traffic-optimization.git](https://github.com/Bloxu1402/smart-traffic-optimization.git)
cd smart-traffic-optimization

2. Install Dependencies
pip install -r requirements.txt

3. Execution
To run the full pipeline, open two separate terminal windows:

Terminal 1 (Computer Vision Detection):

python traffic_detector.py

Terminal 2 (Traffic Logic Controller):

python traffic_controller.py

4. Optimization Algorithm
The system computes green light intervals using a linear scale bounded by safety minimums and maximums to prevent starvation on opposite lanes:

T =max(10,min(10+2.5⋅vehicles,45))
Base Time: 10 seconds minimum.

Scaling Factor: 2.5 seconds added per detected vehicle.

Cap ceiling: 45 seconds maximum.

5.Future Enhancements
Connect the control logic output directly to an Arduino/Raspberry Pi circuit rig using physical LEDs.

Train a Reinforcement Learning (Q-learning) agent to orchestrate grid-wide traffic multi-intersections.

Support emergency vehicle override detection (e.g., detecting ambulance sirens/glowing elements).

Train a Reinforcement Learning (Q-learning) agent to orchestrate grid-wide traffic multi-intersections.

Support emergency vehicle override detection (e.g., detecting ambu
