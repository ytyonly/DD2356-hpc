import matplotlib.pyplot as plt

# Number of MPI processes and their corresponding execution times
num_processes = [8, 16, 32, 64, 128]
execution_times = [2.826138, 1.397551, 1.067055, 0.557696, 0.216521]  # Update with your actual execution times

# Plotting the execution time vs. number of MPI processes
plt.figure(figsize=(8, 6))
plt.plot(num_processes, execution_times, marker='o', color='b', linestyle='-')
plt.title('Execution Time vs. Number of MPI Processes')
plt.xlabel('Number of MPI Processes')
plt.ylabel('Execution Time (seconds)')
plt.grid(True)
plt.xticks(num_processes)
plt.tight_layout()

# Show plot
plt.show()