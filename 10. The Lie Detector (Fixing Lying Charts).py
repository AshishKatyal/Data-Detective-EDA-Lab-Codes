# ============================================
# 🎬 Demo Title: The Lie Detector in Python
# Author: Dr. Ashish Katyal
# ============================================

import matplotlib.pyplot as plt
import numpy as np

print("\n🕵️ Welcome to THE LIE DETECTOR!\n")

# --------------------------------------------
# PART 1: The Story
# --------------------------------------------
print("📌 Part 1: Can Charts Lie?\n")
print("Yes! Poor visualization choices can mislead people.\n")

# Example data (student performance)
years = ["2021", "2022", "2023", "2024"]
marks = [70, 75, 78, 80]

# --------------------------------------------
# PART 2: The Lying Chart (Truncated Axis)
# --------------------------------------------
print("📌 Part 2: The Lying Chart (Manipulated Axis)\n")

plt.figure()
plt.bar(years, marks)

# TRICK: Start y-axis at 65 instead of 0
plt.ylim(65, 85)

plt.title("Student Performance (Misleading)")
plt.ylabel("Marks")
plt.show()

print("👉 Looks like HUGE improvement, right?")
print("❗ But axis is manipulated!\n")

# --------------------------------------------
# PART 3: The Truthful Chart (Correct Axis)
# --------------------------------------------
print("📌 Part 3: The Truthful Chart\n")

plt.figure()
plt.bar(years, marks)

# FIX: Start from zero
plt.ylim(0, 100)

plt.title("Student Performance (Correct)")
plt.ylabel("Marks")
plt.show()

print("👉 Now the change looks realistic!")
print("-" * 50)


# --------------------------------------------
# PART 4: Another Lie (Unequal Bar Width)
# --------------------------------------------
print("\n📌 Part 4: Another Misleading Trick\n")

plt.figure()

# Manipulated bar widths
plt.bar(years, marks, width=[0.2, 0.5, 1.0, 1.5])

plt.title("Misleading Bar Widths")
plt.show()

print("👉 Wider bars look more important!")
print("-" * 50)


# --------------------------------------------
# PART 5: Fixing the Chart
# --------------------------------------------
print("\n📌 Part 5: Fixing the Visualization\n")

plt.figure()

# Equal widths
plt.bar(years, marks, width=0.6)

plt.title("Correct Bar Chart")
plt.show()

print("👉 Equal widths = fair comparison")
print("-" * 50)


# --------------------------------------------
# PART 6: Misleading Line Chart
# --------------------------------------------
print("\n📌 Part 6: Misleading Line Chart\n")

x = np.arange(4)

plt.figure()
plt.plot(x, marks)

# Remove proper labels (misleading context)
plt.title("Growth (Misleading)")
plt.show()

print("👉 Missing labels = confusion!")
print("-" * 50)


# --------------------------------------------
# PART 7: Fixing Line Chart
# --------------------------------------------
print("\n📌 Part 7: Fixing Line Chart\n")

plt.figure()
plt.plot(x, marks)

plt.xticks(x, years)
plt.xlabel("Year")
plt.ylabel("Marks")
plt.title("Student Performance Over Years")
plt.show()

print("👉 Proper labels = clear story")
print("-" * 50)


# --------------------------------------------
# PART 8: Mini Activity
# --------------------------------------------
print("\n📌 Part 8: Try It Yourself!\n")

user_values = input("Enter values (comma separated): ")
data = list(map(float, user_values.split(",")))

plt.figure()
plt.bar(range(len(data)), data)

# Intentionally misleading
plt.ylim(min(data) - 1, max(data))
plt.title("Your Misleading Chart")
plt.show()

print("👉 Now fix it yourself by setting proper axis!\n")

plt.figure()
plt.bar(range(len(data)), data)
plt.ylim(0, max(data) + 5)
plt.title("Your Correct Chart")
plt.show()

print("\n🎉 You exposed the lie!")