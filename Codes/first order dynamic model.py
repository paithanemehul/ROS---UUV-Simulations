import matplotlib.pyplot as plt
import numpy as np

# Define the gain and time constant of the thrusters
K = 0.8
tau = 0.5

# Generate some input values
inputs = np.linspace(0, 1, 101)

# Calculate the corresponding output values
outputs = K * (1 - np.exp(-inputs/tau)) * inputs

# Plot the input vs. output graph
plt.plot(inputs, outputs)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('First-Order Dynamic Model for Rexrov2 Thrusters')
plt.show()
