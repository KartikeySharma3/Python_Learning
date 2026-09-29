"""
Program to convert total seconds into days, hours, minutes, and seconds,
and calculate the equivalent days on another planet.
"""

def convert_seconds():
    try:
        total_seconds = int(input("Enter total seconds: "))

        days = total_seconds // 86400
        remaining_seconds = total_seconds % 86400

        hours = remaining_seconds // 3600
        minutes = (remaining_seconds % 3600) // 60
        seconds = remaining_seconds % 60

        print(f"\n{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")

        planet = input("\nEnter the name of the planet: ").strip()
        planet_seconds = int(input(f"Enter the length of a day on {planet} (in seconds): "))

        if planet_seconds <= 0:
            print("Day length must be greater than 0.")
            return

        planet_days = total_seconds / planet_seconds
        print(f"{total_seconds} seconds is equal to {planet_days:.2f} {planet} day(s).")

    except ValueError:
        print("Invalid input! Please enter valid integers for seconds.")


if __name__ == "__main__":
    convert_seconds()