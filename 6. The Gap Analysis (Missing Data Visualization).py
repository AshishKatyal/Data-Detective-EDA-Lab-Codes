# ============================================
# 🎬 Demo Title: The Gap Analysis in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Install missingno if not already installed
# pip install missingno

import missingno as msno

print("\n🔍 Welcome to THE GAP ANALYSIS!\n")

# --------------------------------------------
# PART 1: What is Missing Data?
# --------------------------------------------
print("📌 Part 1: Understanding Missing Data\n")
print("Missing data = values that are not available (NaN)")
print("It can affect analysis and model performance!\n")

# --------------------------------------------
# PART 2: Create Dataset with Missing Values
# --------------------------------------------
print("📌 Part 2: Creating Dataset with Gaps\n")

np.random.seed(42)

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H"],
    "Age": [25, np.nan, 30, 22, np.nan, 28, 35, np.nan],
    "Marks": [80, 75, np.nan, 90, 85, np.nan, 88, 92],
    "Salary": [50000, 60000, np.nan, np.nan, 55000, 52000, np.nan, 58000]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)
print("-" * 50)


# --------------------------------------------
# PART 3: Basic Missing Value Check
# --------------------------------------------
print("\n📌 Part 3: Checking Missing Values\n")

print("Total Missing Values per Column:\n")
print(df.isnull().sum())

print("\nPercentage Missing:\n")
print((df.isnull().sum() / len(df)) * 100)

print("-" * 50)


# --------------------------------------------
# PART 4: Missingno Matrix Plot
# --------------------------------------------
print("\n📌 Part 4: Visualizing Missing Data (Matrix)\n")

msno.matrix(df)
plt.title("Missing Data Matrix")
plt.show()

print("👉 White lines = Missing data (gaps)")
print("👉 Continuous lines = Complete data")

print("-" * 50)


# --------------------------------------------
# PART 5: Missingno Bar Plot
# --------------------------------------------
print("\n📌 Part 5: Missing Data Summary (Bar Chart)\n")

msno.bar(df)
plt.title("Missing Data Count")
plt.show()

print("👉 Taller bars = More available data")

print("-" * 50)


# --------------------------------------------
# PART 6: Missingno Heatmap (Correlation)
# --------------------------------------------
print("\n📌 Part 6: Missing Data Correlation\n")

msno.heatmap(df)
plt.title("Missing Data Correlation Heatmap")
plt.show()

print("👉 Shows if missing values are related!")

print("-" * 50)


# --------------------------------------------
# PART 7: Why Missing Data Matters
# --------------------------------------------
print("\n📌 Part 7: Why It Matters\n")

print("Missing data can:")
print("• Bias your results")
print("• Reduce accuracy")
print("• Mislead conclusions")

print("-" * 50)


# --------------------------------------------
# PART 8: Mini Activity
# --------------------------------------------
print("\n📌 Part 8: Try It Yourself!\n")

user_data = {
    "A": [1, 2, np.nan, 4],
    "B": [np.nan, 2, 3, 4],
    "C": [1, np.nan, np.nan, 4]
}

user_df = pd.DataFrame(user_data)

print("Your Dataset:\n", user_df)

msno.matrix(user_df)
plt.title("Your Missing Data Matrix")
plt.show()

print("\n🎉 You have successfully visualized missing data!")