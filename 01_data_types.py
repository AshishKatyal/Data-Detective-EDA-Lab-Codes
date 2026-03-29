# ============================================
# 🎬 Demo Title: Understanding Data Types in Python
# Author: Dr. Ashish Katyal
# ============================================

print("\n🎯 Welcome to the World of Python Data Types!\n")

# --------------------------------------------
# PART 1: What is a Data Type?
# --------------------------------------------
print("📌 Part 1: What is a Data Type?")
print("A Data Type defines the kind of value a variable can hold.\n")

# Example
x = 10
print("Example: x = 10")
print("Value of x:", x)
print("Type of x:", type(x))
print("-" * 50)


# --------------------------------------------
# PART 2: Basic Data Types
# --------------------------------------------
print("\n📌 Part 2: Basic Data Types\n")

# Integer
a = 25
print("Integer Example:")
print("a =", a, "| Type:", type(a))

# Float
b = 3.14
print("\nFloat Example:")
print("b =", b, "| Type:", type(b))

# String
c = "Hello Students!"
print("\nString Example:")
print("c =", c, "| Type:", type(c))

# Boolean
d = True
print("\nBoolean Example:")
print("d =", d, "| Type:", type(d))

print("-" * 50)


# --------------------------------------------
# PART 3: Collection Data Types
# --------------------------------------------
print("\n📌 Part 3: Collection Data Types\n")

# List (Mutable)
my_list = [1, 2, 3, 4]
print("List Example:")
print("my_list =", my_list, "| Type:", type(my_list))

# Tuple (Immutable)
my_tuple = (10, 20, 30)
print("\nTuple Example:")
print("my_tuple =", my_tuple, "| Type:", type(my_tuple))

# Set (Unique elements)
my_set = {1, 2, 3, 3, 2}
print("\nSet Example (duplicates removed automatically):")
print("my_set =", my_set, "| Type:", type(my_set))

# Dictionary (Key-Value pairs)
my_dict = {"name": "Ashish", "role": "Professor"}
print("\nDictionary Example:")
print("my_dict =", my_dict, "| Type:", type(my_dict))

print("-" * 50)


# --------------------------------------------
# PART 4: Type Conversion (Casting)
# --------------------------------------------
print("\n📌 Part 4: Type Conversion\n")

num = "100"
print("Original value:", num, "| Type:", type(num))

converted_num = int(num)
print("After conversion:", converted_num, "| Type:", type(converted_num))

print("-" * 50)


# --------------------------------------------
# PART 5: Interactive Learning
# --------------------------------------------
print("\n📌 Part 5: Quick Activity (Try Yourself!)\n")

user_input = input("Enter something: ")

print("\nYou entered:", user_input)
print("Detected Type:", type(user_input))

print("\n⚠️ Note: input() always takes data as STRING by default!")

print("-" * 50)


# --------------------------------------------
# PART 6: Mini Challenge
# --------------------------------------------
print("\n📌 Part 6: Mini Challenge\n")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integers
num1 = int(num1)
num2 = int(num2)

sum_result = num1 + num2

print("Sum =", sum_result)
print("Type of result:", type(sum_result))

print("\n🎉 Congratulations! You have learned Python Data Types!")
