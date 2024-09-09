import matplotlib.pyplot as plt
import numpy as np

# Define the gain of the thrusters
K = 0.8

# Generate some input values
inputs = np.linspace(0, 1, 101)

# Calculate the corresponding output values
outputs = K * inputs

# Plot the input vs. output graph
plt.plot(inputs, outputs)
plt.xlabel('Time')
plt.ylabel('Rotor angular velocity')
plt.title('Zero-Order Dynamic Model for Rexrov2 Thrusters')
plt.show()
