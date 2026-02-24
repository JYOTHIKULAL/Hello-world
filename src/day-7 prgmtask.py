import random
robot_name = input("Enter robot name: ")
target_distance = int(input("Enter distance to target (in meters): "))
obstacle_ahead = input("Is there an obstacle ahead? (yes/no): ").lower()

# ----------- INITIAL SETUP -----------
speed = 0
distance_travelled = 0
checkpoints = []

# ----------- DECISION MAKING -----------
if obstacle_ahead == "yes":
    if target_distance > 50:
        speed = 5
        movement = "Slow movement due to obstacle"
    else:
        speed = 3
        movement = "Very slow and careful movement"
else:
    if target_distance > 100:
        speed = 15
        movement = "Fast movement"
    elif target_distance > 50:
        speed = 10
        movement = "Moderate movement"
    else:
        speed = 6
        movement = "Slow movement"

# ----------- JOURNEY SIMULATION -----------
for i in range(1, 4):
    direction = random.choice(["North", "South", "East", "West"])
    checkpoint = f"Checkpoint {i} - Direction: {direction}"
    checkpoints.append(checkpoint)
    distance_travelled += speed * 5  # simulated distance

# ----------- UPDATE CHECKPOINTS -----------
add_cp = input("Do you want to add an extra checkpoint? (yes/no): ").lower()
if add_cp == "yes":
    checkpoints.append("Extra Checkpoint - Manual Update")

remove_cp = input("Do you want to remove the last checkpoint? (yes/no): ").lower()
if remove_cp == "yes" and checkpoints:
    checkpoints.pop()

# ----------- TRIP SUMMARY -----------
print("\n----- ROBOT TRIP SUMMARY -----")
print(f"Robot Name           : {robot_name}")
print(f"Target Distance      : {target_distance} meters")
print(f"Distance Travelled   : {distance_travelled} meters")
print(f"Obstacle Ahead       : {obstacle_ahead}")
print(f"Movement Type        : {movement}")
print(f"Final Speed          : {speed} m/s")
print(f"Checkpoints Covered  : {checkpoints}")
print("Trip Status          : Mission Completed 🚀")
