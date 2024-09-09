import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

# Define the parameters of the Bessa dynamic model
m = 1
c = 0.5
k = 1
Kp = 1

# Define the initial conditions of the thruster
x0 = 0
dx0 = 0

# Define the input signal to the thruster
t = np.linspace(0, 10, 101)
u = np.sin(t)

# Define the differential equation of the Bessa dynamic model
def bessa(x, t, m, c, k, Kp, u):
    dx = x[1]
    ddx = (Kp*u[t] - c*dx - k*x[0]) / m
    return [dx, ddx]

# Solve the differential equation using the odeint function
sol = odeint(bessa, [x0, dx0], t, args=(m, c, k, Kp, u))

# Plot the input and output signals
plt.plot(t, u, label='Input')
plt.plot(t, sol[:, 0], label='Output')
plt.xlabel('Time')
plt.ylabel('Position')
plt.title('Bessa Dynamic Model for Rexrov2 Thrusters')
plt.legend()
plt.show()
