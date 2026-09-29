"""
Program to calculate the average marks of three subjects.
"""

def calculate_average():
    try:
        num1 = float(input("Enter marks for Subject 1: "))
        num2 = float(input("Enter marks for Subject 2: "))
        num3 = float(input("Enter marks for Subject 3: "))

        average = (num1 + num2 + num3) / 3
        print(f"\nThe average marks are: {average:.2f}")
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")


if __name__ == "__main__":
    calculate_average()