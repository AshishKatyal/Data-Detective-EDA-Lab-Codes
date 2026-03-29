# ============================================
# 🎬 Demo Title: The Outlier Hunt in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n🕵️ Welcome to THE OUTLIER HUNT!\n")

# --------------------------------------------
# PART 1: The Story Begins
# --------------------------------------------
print("📌 Part 1: What is an Outlier?\n")
print("An outlier is a data point that behaves very differently from others.")
print("It can be due to error or a rare event.\n")

# --------------------------------------------
# PART 2: Create Dataset
# --------------------------------------------
print("📌 Part 2: Creating Dataset\n")

np.random.seed(42)

# Normal data
data = np.random.normal(loc=60, scale=8, size=100)

# Add suspicious values (outliers)
suspects = [120, 5, 130]
data = np.concatenate([data, suspects])

df = pd.DataFrame(data, columns=['Marks'])

print("Sample Data:\n", df.head())
print("-" * 50)


# --------------------------------------------
# PART 3: Visual Clue (Box Plot)
# --------------------------------------------
print("\n📌 Part 3: Visual Clue - Box Plot\n")

plt.figure()
plt.boxplot(df['Marks'])
plt.title("Box Plot - Spot the Outliers")
plt.ylabel("Marks")
plt.show()

print("👉 Points outside whiskers are suspicious!")
print("-" * 50)


# --------------------------------------------
# PART 4: Understanding IQR
# --------------------------------------------
print("\n📌 Part 4: Understanding IQR\n")

Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)
IQR = Q3 - Q1

print("Q1 (25th percentile):", Q1)
print("Q3 (75th percentile):", Q3)
print("IQR (Spread of middle data):", IQR)

print("\n👉 IQR focuses on the 'middle crowd'")

print("-" * 50)


# --------------------------------------------
# PART 5: Setting Boundaries (The Rules)
# --------------------------------------------
print("\n📌 Part 5: Finding Boundaries\n")

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\n👉 Anything outside these bounds is an OUTLIER!")

print("-" * 50)


# --------------------------------------------
# PART 6: Catching the Outliers
# --------------------------------------------
print("\n📌 Part 6: Catching the Outliers\n")

outliers = df[(df['Marks'] < lower_bound) | (df['Marks'] > upper_bound)]

print("🚨 Outliers Detected:\n")
print(outliers)

print("-" * 50)


# --------------------------------------------
# PART 7: Highlighting Outliers Visually
# --------------------------------------------
print("\n📌 Part 7: Visual Confirmation\n")

plt.figure()

plt.scatter(range(len(df)), df['Marks'], label="Normal Data")

# Highlight outliers
plt.scatter(outliers.index, outliers['Marks'], label="Outliers")

plt.title("Outlier Detection using IQR")
plt.xlabel("Index")
plt.ylabel("Marks")
plt.legend()
plt.show()


# --------------------------------------------
# PART 8: Mini Activity (Student Engagement)
# --------------------------------------------
print("\n📌 Part 8: Try It Yourself!\n")

user_input = input("Enter marks separated by comma: ")
user_data = list(map(float, user_input.split(",")))

user_df = pd.DataFrame(user_data, columns=['Marks'])

Q1 = user_df['Marks'].quantile(0.25)
Q3 = user_df['Marks'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

user_outliers = user_df[(user_df['Marks'] < lower) | (user_df['Marks'] > upper)]

print("\n🚨 Your Outliers:\n", user_outliers)

print("\n🎉 Case Closed! You are now an Outlier Detective!")
