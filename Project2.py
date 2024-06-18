# Calculates the BMI of the user based on their height and weight and changes the formula based on the measuring system chosen
def BMI(imperial, mass, height):
    if(imperial):
        return 703 * mass / height**2
    else:
        return mass / height**2

# Calculates weight class based on BMI and set standards 
def weightClass(BMI):
    if(BMI <= 18.4):
        return "Underweight"
    elif(BMI <= 24.9):
        return "Normal"
    elif(BMI <= 39.9):
        return "Overweight"
    else:
        return "Obese"

# Allows the user to choose a measuring system  
def system():
    imperial = input("Would you like to calculate your BMI using Imperial(Pounds/Inches) or Metric(Kilogram/Meter)?\nInput I or M: ")
    if(imperial.lower() == "i"):
        return True
    elif(imperial.lower() == "m"):
        return False
    else:
        print("Incorrect Input Please Repeat.")
        return system()

# Runs the BMI calculator
def BMICalculator():  
    print("Welcome to the BMI calculator!")
    imperial = system()

    mass = float(input("Please input your weight in pounds: " if imperial else "Please input your weight in kilograms: "))
    
    # Handles weights out of range
    while(mass >= 500 or mass <= 10):
        mass = float(input("Weight out of range.\nPlease input your weight in pounds: " if imperial else "Weight out of range.\nPlease input your weight in kilograms: "))
    
    height = float(input("Please input your height in inches: " if imperial else "Please input your height in meters: "))
    
    # Handles heights out of range
    while((height >= 2.72 or height < .5) and not imperial):
        height = float(input("Height out of range.\nPlease input your height in meters: "))
    while((height >= 107 or height < 24) and imperial):
        height = float(input("Height out of range.\nPlease input your height in inches: "))

    bmi = BMI(imperial, mass, height)
    print("Your BMI is: %.3f" % bmi, " and your BMI calssification is: ", weightClass(bmi))

BMICalculator()