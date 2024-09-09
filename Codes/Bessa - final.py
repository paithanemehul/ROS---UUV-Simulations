import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the Bessa dynamic model
dt = 0.01
Kt = 0.1
Rm = 1
Kv1 = 0.01
Kv2 = 0.001
Omega_ref = 10

# Define the initial and final time and the initial motor speed
t0 = 0
tf = 10
Omega0 = 0

# Define a function that simulates the Bessa dynamic model
def bessa_model(Omega0, t0, tf, dt, Kt, Rm, Kv1, Kv2, Omega_ref):
    Omega = np.zeros(int((tf - t0) / dt) + 1)
    Omega[0] = Omega0
    for i in range(len(Omega) - 1):
        Omega[i+1] = Omega[i] + dt * (Kt/Rm * Omega_ref - (Kv1 + Kv2 * abs(Omega[i])) * Omega[i])
    return Omega

# Simulate the Bessa dynamic model and plot the results
t = np.arange(t0, tf + dt, dt)
Omega = bessa_model(Omega0, t0, tf, dt, Kt, Rm, Kv1, Kv2, Omega_ref)
plt.plot(t, Omega)
plt.xlabel('Time (s)')
plt.ylabel('Thruster speed (rad/s)')
