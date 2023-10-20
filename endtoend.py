import numpy as np
import matplotlib.pyplot as plt

x1, y1, z1, x2, y2, z2 = np.loadtxt("endtoend.txt", unpack=True)

lines = len(x1)

ete_distance = []
time_step = []

averagingsq_list = []
averaging_list = []

total_dist_sq = 0
total_steps = 0


def window(size):
    return np.ones(size)/float(size)


for i in range(lines):
    distance = np.sqrt(
        pow(x1[i] - x2[i], 2) +
        pow(y1[i] - y2[i], 2) +
        pow(z1[i] - z2[i], 2)
    )

    ete_distance.append(distance)
    time_step.append(i)

    if (i >= 0.9 * lines):
        # total_dist_sq += pow(distance, 2)
        averagingsq_list.append(pow(distance, 2))
        averaging_list.append(distance)
        total_steps += 1

rms_val = np.sqrt(sum(averagingsq_list) / len(averagingsq_list))
stddevdist = np.std(averaging_list)

rms_val = round(rms_val, 3)
stddevdist = round(stddevdist, 3)

print("RMS end-to-end distance =", rms_val, "+/-", stddevdist)


plt.plot(time_step, ete_distance, label="Raw data")
# plt.plot(time_step, np.convolve(ete_distance, window(50), 'same'),
#          label="time averaged")
plt.show()
