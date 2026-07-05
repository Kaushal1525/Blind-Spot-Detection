import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon, Circle
import random


lane_width = 3.5
num_lanes = 3
highway_length = 100
car_length, car_width = 4, 2
car_x, car_y = 20, lane_width * 1.5
car_speed = 0.2
blind_spot_angle = 45
blind_spot_distance = 10
detection_range = 15


fig, ax = plt.subplots(figsize=(12, 6))
ax.set_xlim(0, highway_length)
ax.set_ylim(0, lane_width * num_lanes)
ax.set_title("Blind Spot Monitoring System")
ax.set_xlabel("Highway (meters)")
ax.set_ylabel("Lanes")
ax.set_aspect("equal")

for i in range(1, num_lanes):
    ax.axhline(i * lane_width, color="gray", linestyle="--", linewidth=1)


car = plt.Rectangle((car_x - car_length / 2, car_y - car_width / 2), car_length, car_width, color="blue", zorder=2)
ax.add_patch(car)


vehicles = []
for _ in range(6):
    x = random.randint(0, highway_length)
    lane = random.choice([0, 2])
    y = lane * lane_width + lane_width / 2
    vehicle = plt.Rectangle((x, y - car_width / 2), car_length, car_width, color="green", zorder=3)
    vehicles.append(vehicle)
    ax.add_patch(vehicle)


blind_spot_polygon = Polygon([[0, 0]], closed=True, color="lightblue", alpha=0.5, zorder=1)
ax.add_patch(blind_spot_polygon)


detection_circle = Circle((car_x, car_y), detection_range, color="gray", fill=False, linestyle="--", zorder=0)
ax.add_patch(detection_circle)

alert_text = ax.text(highway_length * 0.6, lane_width * num_lanes * 0.9, "", fontsize=12, color="red", fontweight="bold", zorder=4)

def get_blind_spot_region(car_x, car_y):
    angle_rad = np.radians(blind_spot_angle)
    v1 = (car_x, car_y)
    v2 = (car_x - blind_spot_distance * np.cos(angle_rad), car_y - lane_width / 2 - blind_spot_distance * np.sin(angle_rad))
    v3 = (car_x - blind_spot_distance * np.cos(-angle_rad), car_y + lane_width / 2 - blind_spot_distance * np.sin(-angle_rad))
    return [v1, v2, v3]

def update_vehicle_positions():
    for vehicle in vehicles:
        x, y = vehicle.get_xy()
        x += 0.3
        if x > highway_length:
            x = 0
            lane = random.choice([0, 2])
            y = lane * lane_width + lane_width / 2
        vehicle.set_xy((x, y))

def check_blind_spot(car_x, car_y):
    blind_spot_vertices = get_blind_spot_region(car_x, car_y)
    blind_spot_polygon.set_xy(blind_spot_vertices)
    detection_circle.center = (car_x, car_y)

    is_vehicle_in_blind_spot = False
    for vehicle in vehicles:
        vehicle_center = (vehicle.get_x() + car_length / 2, vehicle.get_y() + car_width / 2)
        distance_to_car = np.hypot(vehicle_center[0] - car_x, vehicle_center[1] - car_y)

        if distance_to_car <= detection_range:
            if Polygon(blind_spot_vertices).contains_point(vehicle_center):
                vehicle.set_color("red")
                is_vehicle_in_blind_spot = True
            else:
                vehicle.set_color("green")
        else:
            vehicle.set_color("green")

    if is_vehicle_in_blind_spot:
        blind_spot_polygon.set_color("red")
        alert_text.set_text("Warning: Vehicle in Blind Spot!")
    else:
        blind_spot_polygon.set_color("lightblue")
        alert_text.set_text("")


def update(frame):
    global car_x
    car_x += car_speed
    if car_x > highway_length:
        car_x = 0

    car.set_xy((car_x - car_length / 2, car_y - car_width / 2))
    update_vehicle_positions()
    check_blind_spot(car_x, car_y)

    return car, blind_spot_polygon, detection_circle, alert_text, *vehicles


ani = FuncAnimation(fig, update, frames=500, interval=50, blit=False)
plt.show()