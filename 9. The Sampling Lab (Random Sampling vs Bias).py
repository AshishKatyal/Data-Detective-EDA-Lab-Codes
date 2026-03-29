# ============================================
# 🎬 Demo Title: The Sampling Lab in Python
# Author: Dr. Ashish Katyal
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("\n🧪 Welcome to THE SAMPLING LAB!\n")

# --------------------------------------------
# PART 1: What is Sampling?
# --------------------------------------------
print("📌 Part 1: Understanding Sampling\n")
print("Sampling = selecting a subset from a population")
print("Goal: Represent the population correctly\n")

# --------------------------------------------
# PART 2: Create Population Data
# --------------------------------------------
print("📌 Part 2: Creating Population\n")

np.random.seed(42)

# Population: student marks (normal distribution)
population = np.random.normal(loc=70, scale=10, size=1000)

print("Population Mean:", np.mean(population))
print("-" * 50)


# --------------------------------------------
# PART 3: Random Sampling (Good Practice)
# --------------------------------------------
print("\n📌 Part 3: Random Sampling\n")

random_sample = np.random.choice(population, size=100, replace=False)

print("Random Sample Mean:", np.mean(random_sample))

# Visualization
plt.figure()
plt.hist(population, bins=30, alpha=0.5, label="Population")
plt.hist(random_sample, bins=30, alpha=0.7, label="Random Sample")
plt.legend()
plt.title("Random Sampling vs Population")
plt.show()

print("👉 Random sample closely represents the population")
print("-" * 50)


# --------------------------------------------
# PART 4: Biased Sampling (Wrong Practice)
# --------------------------------------------
print("\n📌 Part 4: Biased Sampling\n")

# Example bias: selecting only high performers
biased_sample = population[population > 80]

# Take first 100 values
biased_sample = biased_sample[:100]

print("Biased Sample Mean:", np.mean(biased_sample))

# Visualization
plt.figure()
plt.hist(population, bins=30, alpha=0.5, label="Population")
plt.hist(biased_sample, bins=30, alpha=0.7, label="Biased Sample")
plt.legend()
plt.title("Biased Sampling vs Population")
plt.show()

print("👉 Biased sample gives misleading results!")
print("-" * 50)


# --------------------------------------------
# PART 5: Comparing Results
# --------------------------------------------
print("\n📌 Part 5: Comparison\n")

print("Population Mean:", np.mean(population))
print("Random Sample Mean:", np.mean(random_sample))
print("Biased Sample Mean:", np.mean(biased_sample))

print("\n👉 Which one is closer to population? (Think!)")

print("-" * 50)


# --------------------------------------------
# PART 6: Why Bias is Dangerous
# --------------------------------------------
print("\n📌 Part 6: Why Bias Matters\n")

print("Bias can:")
print("• Mislead conclusions")
print("• Produce wrong predictions")
print("• Affect fairness in decision-making")

print("-" * 50)


# --------------------------------------------
# PART 7: Mini Activity
# --------------------------------------------
print("\n📌 Part 7: Try It Yourself!\n")

user_data = input("Enter numbers (comma separated): ")
data = np.array(list(map(float, user_data.split(","))))

# Random sample
sample = np.random.choice(data, size=min(5, len(data)), replace=False)

print("\nYour Random Sample:", sample)
print("Sample Mean:", np.mean(sample))
print("Population Mean:", np.mean(data))

print("\n🎉 You performed sampling!")