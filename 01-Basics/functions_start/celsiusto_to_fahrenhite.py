"""
Program to convert temperature from Celsius to Fahrenheit.
Formula: F = (C * 9/5) + 32
"""

def celsius_to_fahrenheit():
    try:
        celsius = float(input("Enter temperature in Celsius (°C): "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        print("Invalid input! Please enter a valid number for temperature.")


if __name__ == "__main__":
    celsius_to_fahrenheit()