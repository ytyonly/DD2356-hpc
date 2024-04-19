import numpy as np
import matplotlib.pyplot as plt

copy_rates = {
    '1_thread': [11865.9, 10484.9, 11746.7, 11519.1, 8593.9, 11865.9, 10381.5],
    '32_thread': [33522.6, 34437.8, 34624.3, 35428.6],
    '64_thread': [29907.2, 28514.5, 29460.8, 29712.6, 30447.3, 29678.4, 30019.6],
    '128_thread': [22099.3, 21237.0, 22525.8, 21830.4, 21941.8, 23157.8]
}

results = {}

# Calculate averages and standard deviations for each thread count
for thread_count, rates in copy_rates.items():
    average = np.mean(rates)
    std_dev = np.std(rates, ddof=1)  # using Bessel's correction for sample std deviation
    results[thread_count] = {
        'average': average,
        'std_dev': std_dev
    }

results

# Data from the results
thread_counts = ['1', '32', '64', '128']
averages = [results['1_thread']['average'],
            results['32_thread']['average'],
            results['64_thread']['average'],
            results['128_thread']['average']]
std_devs = [results['1_thread']['std_dev'],
            results['32_thread']['std_dev'],
            results['64_thread']['std_dev'],
            results['128_thread']['std_dev']]

thread_counts_int = [int(tc) for tc in thread_counts]

plt.figure(figsize=(10, 5))
plt.errorbar(thread_counts_int, averages, yerr=std_devs, fmt='o-', ecolor='g', capthick=2, capsize=5)
plt.title('STREAM Benchmark - Copy Kernel Bandwidth with Error Bars')
plt.xlabel('Number of Threads')
plt.ylabel('Average Bandwidth (MB/s)')
plt.xticks(thread_counts_int)
plt.grid(True)
plt.show()