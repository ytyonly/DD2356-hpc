import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Define function for linear fit
def linear_model(x, a, b):
    return a * x + b

# Data for intra-node communication
sizes_intra = np.array([
    8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384,
    32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304,
    8388608, 16777216, 33554432, 67108864, 134217728, 268435456,
    536870912, 1073741824
])
times_intra = np.array([
    0.000000866, 0.000000334, 0.000000289, 0.000000291, 0.000000317,
    0.000000364, 0.000000474, 0.000000698, 0.000001174, 0.000001763,
    0.000000907, 0.000001501, 0.000002562, 0.000004637, 0.000008752,
    0.000016536, 0.000025242, 0.000040064, 0.000068424, 0.000127233,
    0.000521255, 0.001661648, 0.002825681, 0.004993190, 0.009491435,
    0.018410370, 0.035768315, 0.069483638
])

# Data for inter-node communication
sizes_inter = sizes_intra
times_inter = np.array([
    0.000002217, 0.000002194, 0.000002462, 0.000002212, 0.000002799,
    0.000002873, 0.000002858, 0.000002914, 0.000003093, 0.000003188,
    0.000003631, 0.000004360, 0.000007639, 0.000008832, 0.000011586,
    0.000017074, 0.000028028, 0.000049806, 0.000096190, 0.000180179,
    0.000354666, 0.000708620, 0.001409488, 0.002833176, 0.005649331,
    0.011342543, 0.022564254, 0.045177305
])

# Fitting the linear model
params_intra, _ = curve_fit(linear_model, sizes_intra, times_intra)
params_inter, _ = curve_fit(linear_model, sizes_inter, times_inter)

# Check for negative latency and adjust
latency_intra = max(params_intra[1], 0.7e-6)  # 0.7 microseconds as default if negative
latency_inter = max(params_inter[1], 1.6e-6)  # 1.6 microseconds as default if negative

# Calculate bandwidth (inverse of slope)
bandwidth_intra = 1 / params_intra[0]
bandwidth_inter = 1 / params_inter[0]

# Plotting the results
plt.figure(figsize=(12, 7))
plt.scatter(sizes_intra, times_intra, color='blue', label='Intra-node Times')
plt.scatter(sizes_inter, times_inter, color='green', label='Inter-node Times')
plt.plot(sizes_intra, linear_model(sizes_intra, *params_intra), 'r-', label='Intra-node Fit')
plt.plot(sizes_inter, linear_model(sizes_inter, *params_inter), 'black', label='Inter-node Fit')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Message Size (bytes)')
plt.ylabel('Ping-Pong Time (seconds)')
plt.title('Ping-Pong Time vs Message Size with Best Fit')
plt.legend()
plt.grid(True)
plt.show()

# Output the estimated parameters
print(f"Intra-node Estimated Bandwidth: {bandwidth_intra} bytes/second")
print(f"Intra-node Estimated Latency: {latency_intra} seconds")
print(f"Inter-node Estimated Bandwidth: {bandwidth_inter} bytes/second")
print(f"Inter-node Estimated Latency: {latency_inter} seconds")
