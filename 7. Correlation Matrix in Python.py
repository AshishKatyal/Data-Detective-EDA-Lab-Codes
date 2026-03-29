# ============================================
# 🎬 Demo Title: Correlation Matrix in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n📊 Welcome! Understanding Correlation Matrix\n")

# --------------------------------------------
# PART 1: What is Correlation?
# --------------------------------------------
print("📌 Part 1: Understanding Correlation\n")
print("Correlation tells us how two variables are related.")
print("Range: -1 to +1")
print("+1 → Strong positive relation")
print("-1 → Strong negative relation")
print(" 0 → No relation\n")

# --------------------------------------------
# PART 2: Create Dataset
# --------------------------------------------
print("📌 Part 2: Creating Dataset\n")

np.random.seed(42)

# Create related data
study_hours = np.random.randint(1, 10, 50)
marks = study_hours * 5 + np.random.randint(0, 10, 50)  # positive correlation
sleep_hours = np.random.randint(4, 10, 50)
stress_level = 100 - marks + np.random.randint(0, 10, 50)  # negative correlation

df = pd.DataFrame({
    "Study_Hours": study_hours,
    "Marks": marks,
    "Sleep_Hours": sleep_hours,
    "Stress_Level": stress_level
})

print("Dataset Sample:\n", df.head())
print("-" * 50)


# --------------------------------------------
# PART 3: Compute Correlation Matrix
# --------------------------------------------
print("\n📌 Part 3: Calculating Correlation Matrix\n")

corr_matrix = df.corr()

print("Correlation Matrix:\n")
print(corr_matrix)

print("-" * 50)


# --------------------------------------------
# PART 4: Visualizing Correlation (Heatmap)
# --------------------------------------------
print("\n📌 Part 4: Visualizing Correlation Matrix\n")

plt.figure()
plt.imshow(corr_matrix)

plt.colorbar()
plt.xticks(range(len(corr_matrix.columns)), corr_matrix.columns)
plt.yticks(range(len(corr_matrix.columns)), corr_matrix.columns)

plt.title("Correlation Matrix Heatmap")
plt.show()

print("👉 Dark/strong colors = strong relationships")
print("👉 Light colors = weak relationships")

print("-" * 50)


# --------------------------------------------
# PART 5: Understanding Results
# --------------------------------------------
print("\n📌 Part 5: Interpreting Results\n")

print("Study Hours vs Marks → Strong Positive Correlation")
print("Marks vs Stress → Negative Correlation")
print("Sleep Hours → Weak or no correlation")

print("-" * 50)


# --------------------------------------------
# PART 6: Highlighting Strong Correlations
# --------------------------------------------
print("\n📌 Part 6: Finding Strong Correlations\n")

for col in corr_matrix.columns:
    for row in corr_matrix.index:
        if col != row and abs(corr_matrix.loc[row, col]) > 0.7:
            print(f"Strong correlation between {row} and {col}: {corr_matrix.loc[row, col]:.2f}")

print("-" * 50)


# --------------------------------------------
# PART 7: Mini Activity
# --------------------------------------------
print("\n📌 Part 7: Try It Yourself!\n")

user_data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [2, 4, 6, 8, 10],
    "Z": [5, 3, 6, 2, 1]
}

user_df = pd.DataFrame(user_data)

print("Your Dataset:\n", user_df)

user_corr = user_df.corr()

print("\nYour Correlation Matrix:\n", user_corr)

plt.figure()
plt.imshow(user_corr)

plt.colorbar()
plt.xticks(range(len(user_corr.columns)), user_corr.columns)
plt.yticks(range(len(user_corr.columns)), user_corr.columns)

plt.title("Your Correlation Heatmap")
plt.show()

print("\n🎉 You have successfully created a correlation matrix!")