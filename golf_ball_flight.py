import matplotlib.pyplot as plt
import numpy as np

GRAVITY = 9.8
LAUNCH_ANGLE = 35
VELOCITY = 150
SPIN_RATE = 100

RADIUS_METERS = .00213
MASS_KG = .046

DRAG_COEFFICIENT = 7
AIR_DENSITY = 1.225
LIFT_COEFFICIENT = 5

TIME_STEP = .05

launch_angle_radians = np.deg2rad(LAUNCH_ANGLE)

x_velocity = VELOCITY * np.cos(launch_angle_radians)
y_velocity = VELOCITY * np.sin(launch_angle_radians)

cross_sectional_area = np.pi * (RADIUS_METERS * RADIUS_METERS)

drag_factor = .5 * DRAG_COEFFICIENT * AIR_DENSITY * cross_sectional_area

x = 0
y = 0
time = 0

x_positions = [x]
y_positions = [y]

def magnus_force(vx, vy):
    v = np.sqrt(vx**2 + vy**2)
    fx_M = LIFT_COEFFICIENT * AIR_DENSITY * cross_sectional_area * SPIN_RATE * vy / v
    fy_M = LIFT_COEFFICIENT * AIR_DENSITY * cross_sectional_area * SPIN_RATE * vx / v

    return fx_M, fy_M

while y>=0:
    x_drag = (drag_factor / MASS_KG) * (x_velocity**2)
    y_drag = (drag_factor / MASS_KG) * (y_velocity**2)

    fx_M, fy_M = magnus_force(x_velocity, y_velocity)

    x_velocity += (-x_drag + fx_M) * TIME_STEP
    y_velocity += (-GRAVITY - y_drag + fy_M ) * TIME_STEP

    x += x_velocity * TIME_STEP
    y += y_velocity * TIME_STEP

    x_positions.append(x)
    y_positions.append(y)

    time += TIME_STEP

print(time)

fig, ax = plt.subplots()
ax.plot(x_positions,y_positions)
plt.xlim(0, 1000)
plt.ylim(0,300)

plt.savefig("plt2.png")

plt.show()