"""
Oasis Infobyte Internship - Python Programming
Task 2: BMI Calculator (Beginner Tier)

Calculates Body Mass Index (BMI) using weight in kilograms and
height in metres, then displays the corresponding BMI category.
"""

def get_positive_number(prompt):
    """Read a positive numeric value, retrying when input is invalid."""
    while True:
        raw_value = input(prompt).strip()

        try:
            value = float(raw_value)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        if value <= 0:
            print("Invalid input. Please enter a value greater than zero.")
            continue

        return value


def calculate_bmi(weight, height):
    """Return BMI using weight in kg and height in metres."""
    return weight / (height ** 2)


def classify_bmi(bmi):
    """Return the BMI category using the task's specified ranges."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("=" * 42)
    print("             BMI CALCULATOR")
    print("=" * 42)
    print("Enter your weight in kilograms and height in metres.\n")

    while True:
        weight = get_positive_number("Enter your weight (kg): ")
        height = get_positive_number("Enter your height (m): ")

        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)

        print("\n---------- YOUR RESULT ----------")
        print(f"Your BMI: {bmi:.2f}")
        print(f"BMI Category: {category}")
        print("---------------------------------")

        again = input("\nWould you like to calculate again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("\nThank you for using the BMI Calculator. Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
