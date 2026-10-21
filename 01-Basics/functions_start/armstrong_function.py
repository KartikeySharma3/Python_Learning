"""
Program to check if a number is an Armstrong number.
Example: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
"""

def is_armstrong(number: int) -> bool:
    """Return True if the given number is an Armstrong number, otherwise False."""
    if number < 0:
        return False
    
    num_str = str(number)
    num_digits = len(num_str)
    
    total = sum(int(digit) ** num_digits for digit in num_str)
    return total == number


if __name__ == "__main__":
    # Test cases
    print(f"Is 7688 an Armstrong number? {is_armstrong(7688)}")
    print(f"Is 153 an Armstrong number? {is_armstrong(153)}")

    # Interactive input
    try:
        user_num = int(input("\nEnter an integer to test: "))
        if is_armstrong(user_num):
            print(f"{user_num} is an Armstrong number!")
        else:
            print(f"{user_num} is NOT an Armstrong number.")
    except ValueError:
        print("Please enter a valid integer.")

 
