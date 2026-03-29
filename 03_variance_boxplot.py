# ============================================
# 🎬 Demo Title: Visualizing Variance using Box Plots
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import matplotlib.pyplot as plt

print("\n🎯 Welcome! Today we understand VARIANCE using BOX PLOTS\n")

# --------------------------------------------
# PART 1: What is Variance?
# --------------------------------------------
print("📌 Part 1: Understanding Variance\n")
print("Variance tells us how spread out the data is.")
print("Low variance → data points are close")
print("High variance → data points are spread out\n")

# --------------------------------------------
# PART 2: Create Two Datasets
# --------------------------------------------
print("📌 Part 2: Creating Two Datasets\n")

np.random.seed(42)

# Low variance data (tight spread)
low_variance = np.random.normal(loc=50, scale=5, size=100)

# High variance data (wide spread)
high_variance = np.random.normal(loc=50, scale=20, size=100)

print("Low Variance Dataset Sample:", low_variance[:5])
print("High Variance Dataset Sample:", high_variance[:5])

print("-" * 50)


# --------------------------------------------
# PART 3: Calculate Variance
# --------------------------------------------
print("\n📌 Part 3: Calculating Variance\n")

var_low = np.var(low_variance)
var_high = np.var(high_variance)

print("Variance (Low Spread):", var_low)
print("Variance (High Spread):", var_high)

print("\n👉 Notice how higher spread = higher variance!")

print("-" * 50)


# --------------------------------------------
# PART 4: Visualizing with Box Plots
# --------------------------------------------
print("\n📌 Part 4: Box Plot Visualization\n")

plt.figure()

plt.boxplot([low_variance, high_variance])
plt.xticks([1, 2], ["Low Variance", "High Variance"])
plt.title("Box Plot Comparison of Data Spread")
plt.ylabel("Values")

plt.show()

print("👉 Wider box = higher spread (variance)")
print("👉 Narrow box = lower spread")

print("-" * 50)


# --------------------------------------------
# PART 5: Explaining Box Plot Components
# --------------------------------------------
print("\n📌 Part 5: Understanding Box Plot\n")

print("A box plot shows:")
print("• Median (middle line)")
print("• Q1 (25th percentile)")
print("• Q3 (75th percentile)")
print("• Whiskers (range)")
print("• Outliers (if any)")

print("-" * 50)


# --------------------------------------------
# PART 6: Mini Activity (Student Interaction)
# --------------------------------------------
print("\n📌 Part 6: Try It Yourself!\n")

user_data = input("Enter numbers separated by comma: ")

# Convert input to list
data_list = list(map(float, user_data.split(",")))

# Calculate variance
user_variance = np.var(data_list)

print("\nYour Data Variance:", user_variance)

# Plot user data
plt.figure()
plt.boxplot(data_list)
plt.title("Your Data Box Plot")
plt.show()

print("\n🎉 Great! You visualized variance yourself!")
