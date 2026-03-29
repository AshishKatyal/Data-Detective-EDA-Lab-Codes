# ============================================
# 🎬 Demo Title: Detecting Outliers in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n🎯 Welcome! Today we learn Outlier Detection in Python\n")

# --------------------------------------------
# PART 1: Generate Sample Data
# --------------------------------------------
print("📌 Part 1: Generating Dataset\n")

np.random.seed(42)

# Normal data
data = np.random.normal(loc=50, scale=10, size=100)

# Add outliers
outliers = [120, 130, 5]
data = np.concatenate([data, outliers])

df = pd.DataFrame(data, columns=['Values'])

print("Sample Data:\n", df.head())
print("-" * 50)


# --------------------------------------------
# PART 2: Visualization (Boxplot)
# --------------------------------------------
print("\n📌 Part 2: Visualizing Outliers using Boxplot\n")

plt.figure()
plt.boxplot(df['Values'])
plt.title("Boxplot for Outlier Detection")
plt.ylabel("Values")
plt.show()

print("👉 Points outside whiskers are potential outliers!")
print("-" * 50)


# --------------------------------------------
# PART 3: Z-Score Method
# --------------------------------------------
print("\n📌 Part 3: Detecting Outliers using Z-Score\n")

mean = np.mean(df['Values'])
std = np.std(df['Values'])

print("Mean:", mean)
print("Standard Deviation:", std)

threshold = 3

z_scores = [(x - mean) / std for x in df['Values']]

outliers_z = df[np.abs(z_scores) > threshold]

print("\nOutliers detected (Z-Score method):")
print(outliers_z)

print("-" * 50)


# --------------------------------------------
# PART 4: IQR Method (Most Important)
# --------------------------------------------
print("\n📌 Part 4: Detecting Outliers using IQR Method\n")

Q1 = df['Values'].quantile(0.25)
Q3 = df['Values'].quantile(0.75)
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers_iqr = df[(df['Values'] < lower_bound) | (df['Values'] > upper_bound)]

print("\nOutliers detected (IQR method):")
print(outliers_iqr)

print("-" * 50)


# --------------------------------------------
# PART 5: Visualization with Highlighted Outliers
# --------------------------------------------
print("\n📌 Part 5: Visualizing Outliers Clearly\n")

plt.figure()
plt.scatter(range(len(df)), df['Values'], label='Normal Data')

# Highlight outliers
plt.scatter(outliers_iqr.index, outliers_iqr['Values'], label='Outliers')

plt.title("Outlier Detection (IQR Method)")
plt.xlabel("Index")
plt.ylabel("Values")
plt.legend()
plt.show()


# --------------------------------------------
# PART 6: Mini Activity
# --------------------------------------------
print("\n📌 Part 6: Mini Activity\n")

user_data = input("Enter numbers separated by comma: ")

# Convert input into list
user_list = list(map(float, user_data.split(",")))
user_df = pd.DataFrame(user_list, columns=['Values'])

Q1 = user_df['Values'].quantile(0.25)
Q3 = user_df['Values'].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers_user = user_df[(user_df['Values'] < lower_bound) | (user_df['Values'] > upper_bound)]

print("\nYour Outliers are:")
print(outliers_user)

print("\n🎉 You have successfully learned Outlier Detection!")