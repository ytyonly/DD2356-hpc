import matplotlib.pyplot as plt

# Given computation times for different thread counts
thread_counts = [1, 32, 64, 128]
computation_times = [19.160617, 0.604827, 0.318856, 0.232146]

# Calculating speed-up: T1/Tn
T1 = computation_times[0]  # Time using 1 thread
speed_ups = [T1 / time for time in computation_times]

# Plotting the speed-up graph
plt.figure(figsize=(10, 6))
plt.plot(thread_counts, speed_ups, marker='o', linestyle='-', color='b')
plt.xlabel("Number of Threads")
plt.ylabel("Speed-Up (T1/Tn)")
plt.title("Speed-Up vs. Number of Threads for DFTW Calculation")
plt.grid(True)
plt.xticks(thread_counts)
plt.yticks(range(int(min(speed_ups)), int(max(speed_ups)) + 2))
plt.show()

