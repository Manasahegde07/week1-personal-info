# Personal Information Manager
# Author: Manasa Mahabaleshwar Hegde
# Week 1 Python Basics Project

print("=" * 40)
print("    PERSONAL INFORMATION MANAGER")
print("=" * 40)
print()

name = "Manasa"
age = 21
city = "Bengaluru"
hobby = "Drawing"

print("Please tell me about yourself:")
print("-" * 30)

favorite_food = input("Enter your favorite food: ").strip()
while favorite_food == "":
    print("Food cannot be empty!")
    favorite_food = input("Enter your favorite food: ").strip()

favorite_color = input("Enter your favorite color: ").strip()
while favorite_color == "":
    print("Color cannot be empty!")
    favorite_color = input("Enter your favorite color: ").strip()

age_in_months = age * 12

print()
print("=" * 40)
print("        YOUR INFORMATION")
print("=" * 40)
print()

print(f"Name           : {name}")
print(f"Age            : {age} years ({age_in_months} months)")
print(f"City           : {city}")
print(f"Hobby          : {hobby}")
print()
print(f"Favorite Food  : {favorite_food.title()}")
print(f"Favorite Color : {favorite_color.title()}")
print()

print("=" * 40)
print("Thank you for using the program!")
print("=" * 40)
