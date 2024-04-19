import numpy as np
import matplotlib.pyplot as plt

schedules_data = {
    'static': [23255.7, 25305.0],  # Two runs with static scheduling
    'dynamic': [23141.8, 23894.9],  # Two runs with dynamic scheduling
    'guided': [23999.2, 23137.8]  # Two runs with guided scheduling
}

averages_schedules = {sched: np.mean(vals) for sched, vals in schedules_data.items()}

schedules = list(averages_schedules.keys())
average_bandwidths = [averages_schedules[sched] for sched in schedules]

plt.figure(figsize=(10, 5))
plt.plot(schedules, average_bandwidths, marker='o', color='blue', linestyle='-')
plt.title('Comparison of Bandwidth with Different Schedules using 128 Threads')
plt.xlabel('Scheduling Type')
plt.ylabel('Average Bandwidth (MB/s)')
plt.grid(True, axis='y')
plt.show()