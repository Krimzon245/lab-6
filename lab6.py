# Name: Daniel Momoh
# Date: 2025-06-27

import math

# Part 1: Add a function CelToFahr that converts a temperature from Celsius to Fahrenheit.
def CelToFahr(celsius):
    # Converts a temperature from Celsius to Fahrenheit.

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Part 2: Create a function min. This function receives two arguments and returns the smallest of the two inputs.
def min(num1, num2):
    # Returns the smallest of two input numbers.
    if num1 < num2:
        return num1
    else:
        return num2

# Part 3: Create a function VolumeOfSphere. This function receives one argument,
# the radius of the sphere and returns the volume of the sphere.
def VolumeOfSphere(radius):
    # Calculates the volume of a sphere given its radius.

    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

# --- Test your functions with user inputs ---

print("--- Testing CelToFahr function ---")
try:
    celsius_input = float(input("Enter temperature in Celsius: "))
    print(f"{celsius_input}°C is {CelToFahr(celsius_input):.2f}°F")
except ValueError:
    print("Invalid input. Please enter a number for temperature.")

print("\n--- Testing min function ---")
try:
    num1_input = float(input("Enter the first number: "))
    num2_input = float(input("Enter the second number: "))
    print(f"The minimum of {num1_input} and {num2_input} is: {min(num1_input, num2_input)}")
except ValueError:
    print("Invalid input. Please enter numbers for comparison.")

print("\n--- Testing VolumeOfSphere function ---")
try:
    radius_input = float(input("Enter the radius of the sphere: "))
    volume_result = VolumeOfSphere(radius_input)
    print(f"Volume of a sphere with radius {radius_input}: {volume_result:.2f}")
except ValueError as e:
    print(f"Error: {e}. Please enter a non-negative number for the radius.")