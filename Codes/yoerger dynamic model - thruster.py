import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the motor controller
dt = 0.01
beta = 11
alpha = 0.5
Omega_ref = 10

# Define the initial and final time and the initial motor speed
t0 = 0
tf = 10
Omega0 = 0

# Define a function that simulates the motor controller
def motor_controller(Omega0, t0, tf, dt, beta, alpha, Omega_ref):
    Omega = np.zeros(int((tf - t0) / dt) + 1)
    Omega[0] = Omega0
    for i in range(len(Omega) - 1):
        Omega[i+1] = Omega[i] + dt * (beta * Omega_ref - alpha * Omega[i] * abs(Omega[i]))
    return Omega

# Simulate the motor controller and plot the results
t = np.arange(t0, tf + dt, dt)
Omega = motor_controller(Omega0, t0, tf, dt, beta, alpha, Omega_ref)
plt.plot(t, Omega)
plt.xlabel('Time (s)')
plt.ylabel('Motor angular velocity (rad/s)')
plt.title('Motor control using PD controller')
plt.show()
