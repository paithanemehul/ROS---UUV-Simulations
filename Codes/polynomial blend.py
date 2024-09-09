import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def polynomial_blend(start, end, start_direction, end_direction, t):
    """
    Computes a polynomial blend between two segments based on the start and end points,
    start and end directions, and a time parameter t.
    """
    delta = end - start
    direction = (1 - t) * start_direction + t * end_direction
    direction /= np.linalg.norm(direction)
    length = np.linalg.norm(delta)
    h00 = (1 + 2 * t) * (1 - t) ** 2
    h10 = t * (1 - t) ** 2
    h01 = t ** 2 * (3 - 2 * t)
    h11 = t ** 2 * (t - 1)
    position = start + delta * (h00 + h10 + h01 + h11)
    return position, direction

def generate_path(start, end, num_segments, segment_length):
    """
    Generates a smooth path between a start and end point using a specified number of segments
    and segment length, with polynomial blends used to connect the segments.
    """
    delta = end - start
    direction = delta / np.linalg.norm(delta)
    segment_delta = delta / num_segments
    segment_direction = direction / num_segments
    path = [start]
    for i in range(num_segments):
        start_segment = start + i * segment_delta
        end_segment = start + (i + 1) * segment_delta
        start_direction = segment_direction * i
        end_direction = segment_direction * (i + 1)
        for j in range(segment_length):
            t = j / segment_length
            position, direction = polynomial_blend(start_segment, end_segment, start_direction, end_direction, t)
            path.append(position)
    path.append(end)
    return np.array(path)

# Define start and end points
start = np.array([0, 0, 0])
end = np.array([10, 10, 10])

# Generate path
num_segments = 10
segment_length = 10
path = generate_path(start, end, num_segments, segment_length)

# Plot path in 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = path[:, 0]
y = path[:, 1]
z = path[:, 2]
ax.plot(x, y, z, color='b', linewidth=2)
ax.scatter(start[0], start[1], start[2], color='r', marker='o', s=100)
ax.scatter(end[0], end[1], end[2], color='g', marker='o', s=100)
plt.show()
