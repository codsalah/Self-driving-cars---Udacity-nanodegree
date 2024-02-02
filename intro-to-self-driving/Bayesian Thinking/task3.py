# Create a List
count_data = [54, 111, 163, 222, 277, 336, 276, 220, 171, 111, 59]

# Sum the Counts
total_count = sum(count_data)

# Calculate a Discrete Probability Distribution
normalized_counts = []
for i in range(len(count_data)):
    normalized_counts.append(count_data[i] / total_count)

print("Original Count Data:", count_data)
print("Total Count:", total_count)
print("Normalized Counts (Probability Distribution):", normalized_counts)