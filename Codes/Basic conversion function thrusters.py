import matplotlib.pyplot as plt
import numpy as np

# Define the conversion constants for the basic conversion function
K = 0.5
b = 0.1

# Define the input signal to the thruster
t = np.linspace(0, 10, 101)
u = np.sin(t)

# Compute the output signal using the basic conversion function
y = K * u + b

# Plot the input and output signals
plt.plot(t, u, label='Input')
plt.plot(t, y, label='Output')
plt.xlabel('Time')
plt.ylabel('Signal')
plt.title('Basic Conversion Function for Rexrov2 Actuators')
plt.legend()
plt.show()
