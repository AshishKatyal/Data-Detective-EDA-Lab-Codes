# ============================================
# 🎬 Demo Title: Histograms vs KDE in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import matplotlib.pyplot as plt

print("\n🎯 Welcome! Understanding Data Shape: Histogram vs KDE\n")

# --------------------------------------------
# PART 1: What is Data Shape?
# --------------------------------------------
print("📌 Part 1: What is Data Shape?\n")
print("Data shape tells us how values are distributed.")
print("Are they symmetric? Skewed? Multi-peaked?\n")

# --------------------------------------------
# PART 2: Generate Sample Data
# --------------------------------------------
print("📌 Part 2: Creating Dataset\n")

np.random.seed(42)

# Normal distribution
normal_data = np.random.normal(loc=50, scale=10, size=1000)

# Skewed data
skewed_data = np.random.exponential(scale=10, size=1000)

print("Datasets created: Normal & Skewed")
print("-" * 50)


# --------------------------------------------
# PART 3: Histogram Visualization
# --------------------------------------------
print("\n📌 Part 3: Histogram\n")

plt.figure()
plt.hist(normal_data, bins=30)
plt.title("Histogram (Normal Data)")
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.show()

print("👉 Histogram shows frequency using bars")
print("👉 Depends on bin size!")

print("-" * 50)


# --------------------------------------------
# PART 4: KDE Visualization (Manual)
# --------------------------------------------
print("\n📌 Part 4: KDE (Smooth Curve)\n")

# Simple KDE function
def kde_manual(data, bandwidth=3):
    x = np.linspace(min(data), max(data), 1000)
    kde_values = []

    for xi in x:
        kernel = np.exp(-0.5 * ((data - xi) / bandwidth) ** 2)
        kde_values.append(np.sum(kernel))

    return x, kde_values

x_kde, y_kde = kde_manual(normal_data)

plt.figure()
plt.plot(x_kde, y_kde)
plt.title("KDE Plot (Normal Data)")
plt.xlabel("Values")
plt.ylabel("Density")
plt.show()

print("👉 KDE shows smooth distribution")
print("👉 No bins involved!")

print("-" * 50)


# --------------------------------------------
# PART 5: Histogram vs KDE (Comparison)
# --------------------------------------------
print("\n📌 Part 5: Histogram vs KDE Comparison\n")

plt.figure()

# Histogram
plt.hist(normal_data, bins=30, alpha=0.5, label="Histogram")

# KDE
x_kde, y_kde = kde_manual(normal_data)
plt.plot(x_kde, y_kde, label="KDE")

plt.title("Histogram vs KDE (Normal Data)")
plt.legend()
plt.show()

print("👉 Histogram = discrete view")
print("👉 KDE = smooth view")

print("-" * 50)


# --------------------------------------------
# PART 6: Skewed Data Comparison
# --------------------------------------------
print("\n📌 Part 6: Skewed Data Visualization\n")

plt.figure()

plt.hist(skewed_data, bins=30, alpha=0.5, label="Histogram")

x_kde, y_kde = kde_manual(skewed_data)
plt.plot(x_kde, y_kde, label="KDE")

plt.title("Histogram vs KDE (Skewed Data)")
plt.legend()
plt.show()

print("👉 Notice how KDE clearly shows skewness!")

print("-" * 50)


# --------------------------------------------
# PART 7: When to Use What?
# --------------------------------------------
print("\n📌 Part 7: When to Use What?\n")

print("Use Histogram when:")
print("• You want exact frequency")
print("• You are teaching basics")
print("• Data size is small\n")

print("Use KDE when:")
print("• You want smooth distribution")
print("• You are analyzing trends")
print("• You want to detect skewness or peaks\n")

print("-" * 50)


# --------------------------------------------
# PART 8: Mini Activity
# --------------------------------------------
print("\n📌 Part 8: Try It Yourself!\n")

user_data = input("Enter numbers separated by comma: ")
data_list = list(map(float, user_data.split(",")))

plt.figure()
plt.hist(data_list, bins=10, alpha=0.5, label="Histogram")

x_kde, y_kde = kde_manual(np.array(data_list))
plt.plot(x_kde, y_kde, label="KDE")

plt.title("Your Data: Histogram vs KDE")
plt.legend()
plt.show()

print("\n🎉 You just visualized your own data shape!")