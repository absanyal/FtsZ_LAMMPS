import numpy as np
import matplotlib.pyplot as plt

x1, y1, z1, x2, y2, z2 = np.loadtxt("endtoend.txt", unpack=True)

lines = len(x1)

ete_distance = []
time_step = []

total_dist_sq = 0
total_steps = 0

for i in range(lines):
    distance = np.sqrt(
        pow(x1[i] - x2[i], 2) +
        pow(y1[i] - y2[i], 2) +
        pow(z1[i] - z2[i], 2)
    )

    ete_distance.append(distance)
    time_step.append(i)
    
    if (i > 0.9 * lines):
        total_dist_sq += pow(distance, 2)
        total_steps += 1

rms_val = np.sqrt( total_dist_sq / total_steps )

print("RMS end-to-end distance =", rms_val)

# plt.plot(time_step, ete_distance)
# plt.show()
