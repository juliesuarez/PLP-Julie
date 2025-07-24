import random
import statistics

# Roll a 6-sided die 100 times
rolls = [random.randint(1, 6) for _ in range(100)]

# Basic statistics
mean = statistics.mean(rolls)
median = statistics.median(rolls)
mode = statistics.mode(rolls)
variance = statistics.variance(rolls)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
print(f"Variance: {variance}")