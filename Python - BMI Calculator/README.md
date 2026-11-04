# BMI Calculator — Oasis Infobyte Internship

**Track:** Python Programming  
**Task:** Task 2 — BMI Calculator  
**Tier:** Beginner

## Objective

Build a Python program that calculates a user's Body Mass Index (BMI) from weight in kilograms and height in metres, then classifies the result into the categories specified in the Oasis Infobyte task list.

## Features

- Prompts for weight (kg) and height (m).
- Calculates BMI using `weight / (height ** 2)`.
- Displays BMI rounded to two decimal places.
- Classifies the result as Underweight, Normal, Overweight, or Obese.
- Handles non-numeric input and values less than or equal to zero.
- Allows repeated calculations without restarting the program.

## BMI categories

| BMI range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 to below 25 | Normal |
| 25 to below 30 | Overweight |
| 30 or above | Obese |

These are the category thresholds specified in the internship task.

## Requirements

- Python 3
- No third-party packages required

## How to run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On some systems, use:

```bash
python3 main.py
```

## Example

```text
==========================================
             BMI CALCULATOR
==========================================
Enter your weight in kilograms and height in metres.

Enter your weight (kg): 65
Enter your height (m): 1.7

---------- YOUR RESULT ----------
Your BMI: 22.49
BMI Category: Normal
---------------------------------

Would you like to calculate again? (y/n): n

Thank you for using the BMI Calculator. Goodbye!
```

## Input validation

- Text or other non-numeric input is rejected with a helpful message.
- Zero and negative values are rejected.
- The program asks again until a valid positive number is entered.

## Project structure

```text
Python-Task2-BMICalculator/
├── main.py
└── README.md
```

## Notes

This is an educational programming project, not a medical diagnostic tool. BMI is a screening measure and does not by itself determine an individual's health.

## Internship checklist

- [x] Weight and height input
- [x] BMI formula
- [x] Four BMI categories
- [x] BMI rounded to two decimal places
- [x] Non-numeric and non-positive input validation
- [x] Repeat calculation option
