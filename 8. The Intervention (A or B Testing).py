# ============================================
# 🎬 Demo Title: The Intervention (A/B Testing)
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

print("\n🧪 Welcome to THE INTERVENTION: A/B Testing!\n")

# --------------------------------------------
# PART 1: What is A/B Testing?
# --------------------------------------------
print("📌 Part 1: Understanding A/B Testing\n")
print("A/B Testing compares two groups:")
print("A → Control (original version)")
print("B → Treatment (new version)\n")

print("Goal: Does B perform better than A?\n")

# --------------------------------------------
# PART 2: Designing the Experiment
# --------------------------------------------
print("📌 Part 2: Designing the Experiment\n")

np.random.seed(42)

# Control group (A)
control = np.random.normal(loc=50, scale=10, size=100)

# Treatment group (B) - slightly improved
treatment = np.random.normal(loc=55, scale=10, size=100)

print("Control Mean:", np.mean(control))
print("Treatment Mean:", np.mean(treatment))

print("-" * 50)


# --------------------------------------------
# PART 3: Visualizing the Groups
# --------------------------------------------
print("\n📌 Part 3: Visual Comparison\n")

plt.figure()
plt.hist(control, bins=20, alpha=0.5, label="Control (A)")
plt.hist(treatment, bins=20, alpha=0.5, label="Treatment (B)")
plt.legend()
plt.title("A/B Test Distribution")
plt.xlabel("Performance")
plt.ylabel("Frequency")
plt.show()

print("👉 Do you see a shift between A and B?")
print("-" * 50)


# --------------------------------------------
# PART 4: Hypothesis Testing
# --------------------------------------------
print("\n📌 Part 4: Hypothesis Testing\n")

print("H0 (Null): No difference between A and B")
print("H1 (Alternative): B is better than A\n")

# Perform t-test
t_stat, p_value = stats.ttest_ind(treatment, control)

print("T-statistic:", t_stat)
print("P-value:", p_value)

print("-" * 50)


# --------------------------------------------
# PART 5: Decision Making
# --------------------------------------------
print("\n📌 Part 5: Decision Time\n")

alpha = 0.05

if p_value < alpha:
    print("✅ Reject Null Hypothesis")
    print("🎉 Treatment (B) is significantly better!")
else:
    print("❌ Fail to Reject Null Hypothesis")
    print("⚠️ No significant difference detected")

print("-" * 50)


# --------------------------------------------
# PART 6: Effect Size (Practical Significance)
# --------------------------------------------
print("\n📌 Part 6: Effect Size\n")

mean_diff = np.mean(treatment) - np.mean(control)

print("Mean Difference:", mean_diff)

print("👉 Statistical significance ≠ Practical significance")

print("-" * 50)


# --------------------------------------------
# PART 7: Mini Activity (Student Engagement)
# --------------------------------------------
print("\n📌 Part 7: Try It Yourself!\n")

user_A = input("Enter Control group values (comma separated): ")
user_B = input("Enter Treatment group values (comma separated): ")

A = np.array(list(map(float, user_A.split(","))))
B = np.array(list(map(float, user_B.split(","))))

t_stat, p_val = stats.ttest_ind(B, A)

print("\nYour Results:")
print("T-statistic:", t_stat)
print("P-value:", p_val)

if p_val < 0.05:
    print("🎉 Significant difference found!")
else:
    print("⚠️ No significant difference")

print("\n🧪 You just performed an A/B test!")