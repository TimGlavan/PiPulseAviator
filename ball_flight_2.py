import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def flightg(t, x):
    drag_coefficient = .15
    r = .002378
    A = .25 * np.pi * (1.75/12)**2
    m = (1.5/(16*32.2))

    drag = (1/2) * drag_coefficient * r * A

    s = .000005
    M = s/m
    W_I = 0
    W_J = 5
    W_K = 120

    xprime = np.zeros(6)

    # X
    xprime[0] = x[1]
    xprime[1] = -(drag/m) * x[1]**2 + M * (W_J * x[5] - W_K * x[3])

    # Y
    xprime[2] = x[3]
    xprime[3] = -32.2 - (drag/m) * x[3]**2 + M * (W_K * x[1] - W_I * x[5])

    # Z
    xprime[4] = x[5]
    xprime[5] = -(drag/m) * x[5]**2 + M * (W_I * x[3] - W_J * x[1])

    return xprime

def hit_ground(t, x):
    return(x[2])

hit_ground.terminal = True
hit_ground.direction = -1

def golfball():

    t_span = (0, 20)
    x0 = [0, 175, 0, 75, 0, 0]
    sol = solve_ivp(flightg, t_span, x0, events=hit_ground, t_eval=np.linspace(0, 20, 1000))

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    ax.plot(sol.y[0], sol.y[4], sol.y[2], '-b', linewidth=2, label='Trajectory')

    max_range = max(max(sol.y[0]), max(abs(sol.y[2])), max(sol.y[4])) * 1.1
    ax.set_xlim(0, max_range)
    ax.set_zlim(0, max_range)
    ax.set_ylim(-max_range/2, max_range/2)

    ax.set_title("Golf Ball Model")
    ax.set_xlabel("X (feet)")
    ax.set_ylabel("Z (feet)")
    ax.set_zlabel("Y (feet)")
    plt.grid(True)
    plt.show()




if __name__ == "__main__":
    golfball()