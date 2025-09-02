# Body Mass Index Calculator
# Write a Python function called calculate_bmi that takes in two parameters:

# weight (a float): represents the weight of the person in kilograms.
#height (a float): represents the height of the person in meters.
# The function should calculate the BMI of the person using the formula:
# BMI = weight / (height * height)

def calculate_bmi(weight: float, height: float) -> float:
    bmi = weight /(height ** 2)
    return round(bmi, 2)

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in m: "))

bmi = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi}")

