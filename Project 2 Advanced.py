import tkinter as tk
from tkinter import messagebox

# Calculates the BMI of the user based on their height and weight and changes the formula based on the measuring system chosen
def BMI(imperial, mass, height):
    if(imperial == "I"):
        result = 703 * mass / height**2
    else:
        result = mass / height**2
    result -= result % .001
    return "Your BMI is: " + str(result) + " and your weight class is " + weightClass(result) 

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

# Runs the BMI calculator
def BMICalculator():  
    imperial = measureSys.get()
    weight = weightVar.get()
    height = heightVar.get()
    
    # Handles weights out of range
    if(weight >= 500 or weight <= 10):
         return messagebox.showerror("Out of Bounds","Weight out of range.\nPlease input your weight in pounds"
                                     if imperial == "I" else "Weight out of range.\nPlease input your weight in kilograms")
    
    # Handles heights out of range
    if((height >= 2.72 or height < .5) and imperial == "M"):
        return messagebox.showerror("Out of Bounds","Height out of range.\nPlease input your height in meters")
    if((height >= 107 or height < 24) and imperial == "I"):
        return messagebox.showerror("Out of Bounds","Height out of range.\nPlease input your height in inches")
    messagebox.showinfo("Result", BMI(imperial, weight, height))

page = tk.Tk()
page.title("BMI Calculator")
measureSys = tk.StringVar()
heightVar = tk.DoubleVar()
weightVar = tk.DoubleVar()
tk.Radiobutton(page, text='Imperial (Pounds/Inches)', variable=measureSys, value='I').grid(row = 0, column = 0)
tk.Radiobutton(page, text='Metric (Kilos/Meters)', variable=measureSys, value='M').grid(row = 0, column = 1)
tk.Label(page, text='Weight').grid(row = 1, pady = 20)
tk.Label(page, text='Height').grid(row = 2, pady = 20)
e1 = tk.Entry(page, textvariable = weightVar).grid(row = 1, column = 1)
e2 = tk.Entry(page, textvariable = heightVar).grid(row = 2, column = 1)
button = tk.Button(page, text="Calculate BMI", command=BMICalculator).grid(row = 3)
page.mainloop()