
# Blind Spot Monitoring System Simulation

## Overview

This project presents a simulation of a Blind Spot Monitoring (BSM) system developed using Python and Matplotlib. The simulation demonstrates how a vehicle can monitor its blind spot region while traveling on a multi-lane highway and detect nearby vehicles that may not be visible to the driver.

The project provides a visual representation of the vehicle's blind spot, detection range, surrounding traffic, and warning alerts. It serves as an educational demonstration of one of the Advanced Driver Assistance Systems (ADAS) technologies used in modern vehicles.

---

## Features

- Multi-lane highway simulation
- Real-time vehicle movement
- Blind spot region visualization
- Vehicle detection within blind spot
- Detection range visualization
- Collision awareness indicator
- Dynamic traffic generation
- Real-time warning alerts
- Animated simulation using Matplotlib
- Simple geometric detection algorithm

---

## Technologies Used

- Python 3
- Matplotlib
- NumPy
- Random

---

## Project Structure

```text
Blind-Spot-Monitoring-System/
│
├── blind_spot_monitoring.py
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Kaushal1525/Blind-Spot-Monitoring-System.git
```

### Navigate to the project directory

```bash
cd Blind-Spot-Monitoring-System
```

### Install the required dependencies

```bash
pip install -r requirements.txt
```

or

```bash
pip install matplotlib numpy
```

---

## Running the Project

Execute the following command:

```bash
python blind_spot_monitoring.py
```

The simulation window will open automatically and begin animating highway traffic with blind spot detection.

---

## Working Principle

1. A three-lane highway environment is created.
2. The ego vehicle moves continuously along the highway.
3. Multiple surrounding vehicles move independently.
4. A blind spot region is generated behind the ego vehicle.
5. A detection zone monitors nearby vehicles.
6. Each vehicle's position is continuously updated.
7. Vehicles entering the blind spot are highlighted.
8. A warning message is displayed whenever another vehicle occupies the blind spot.
9. Vehicles outside the blind spot remain in their normal state.

---

## Simulation Components

### Ego Vehicle

The primary vehicle being monitored during the simulation.

### Traffic Vehicles

Randomly generated surrounding vehicles moving along adjacent lanes.

### Blind Spot Region

A triangular region behind the ego vehicle representing areas that are difficult for the driver to observe using mirrors.

### Detection Range

A circular monitoring region surrounding the vehicle that limits object detection to nearby vehicles.

### Warning System

Displays a visual warning whenever another vehicle enters the blind spot.

---

## Detection Logic

The simulation performs the following steps during each animation frame:

- Update the ego vehicle position.
- Move surrounding traffic vehicles.
- Compute the blind spot polygon.
- Check whether surrounding vehicles lie inside the blind spot.
- Highlight detected vehicles.
- Display or clear the warning message.

---

## Simulation Parameters

| Parameter | Description |
|-----------|-------------|
| Lane Width | Width of each traffic lane |
| Number of Lanes | Total highway lanes |
| Vehicle Speed | Speed of the ego vehicle |
| Blind Spot Angle | Angular spread of blind spot |
| Blind Spot Distance | Length of blind spot region |
| Detection Range | Maximum monitoring distance |

---

## Future Enhancements

- Radar sensor simulation
- LiDAR integration
- Camera-based object detection
- Ultrasonic sensor simulation
- Sensor fusion
- Lane change assistance
- Collision avoidance system
- Adaptive cruise control integration
- Vehicle-to-Vehicle (V2V) communication
- Machine learning-based object detection
- ROS integration
- CARLA simulator implementation
- Autonomous driving support
- Real vehicle sensor integration

---

## Applications

- Advanced Driver Assistance Systems (ADAS)
- Autonomous Vehicles
- Driver Assistance Systems
- Vehicle Safety Research
- Automotive Engineering Education
- Intelligent Transportation Systems
- Robotics Simulation
- Automotive Software Development
- Autonomous Mobility Research

---

## Requirements

- Python 3.8 or later
- Matplotlib
- NumPy

---

## Dependencies

- matplotlib
- numpy

---

## Author

Kaushal Reddy

AI & Autonomous Systems Engineer

GitHub: https://github.com/Kaushal1525
````
