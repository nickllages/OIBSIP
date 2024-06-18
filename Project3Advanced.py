import random as rng
import tkinter as tk
from tkinter import messagebox

# Sets for numbers letters and symbols
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','-','=','+','[',']','{','}','\\','|',';',':','\'','"',',','<','.','>','/','?']

# Generates the random password based on lenght and character types
def passwordGenerator(length, charType):
    password = ""
    for i in range(length):
        if(charType == "num"):
            password += numbers[int(rng.random() * 9)]

        elif(charType == "alpha"):
            password += letters[int(rng.random() * 51)]

        elif(charType == "symbol"):
            password += symbols[int(rng.random() * 29)]

        elif(charType == "alnum"):
            random = int(rng.random() * 61)
            if(random <= 9):
                password += numbers[random]
            else:
                password += letters[random - 10]

        elif(charType == "ls"):
            random = int(rng.random() * 81)
            if(random <= 51):
                password += letters[random]
            else:
                password += symbols[random - 52]

        elif(charType == "ns"):
            random = int(rng.random() * 39)
            if(random <= 9):
                password += numbers[random]
            else:
                password += symbols[random - 10]

        elif(charType == "all"):
            random = int(rng.random() * 91)
            if(random <= 9):
                password += numbers[random]
            elif(random <= 61):
                password += letters[random - 10]
            else:
                password += symbols[random - 62]
    return password

# Allows user to choose character types to be used in the password generator
def charType(nums, chars, syms):
    if(nums):
        if(chars):
            if(syms):
                return "all"
            else:
                return "alnum"
        elif(syms):
            return "ns"
        else:
            return "num"
    
    elif(chars):
        if(syms):
            return "ls"
        else:
            return "alpha"
    
    elif(syms):
        return "symbol"

# Runs the command line password generator
def randomPasswordGenerator():
    length = passLength.get()
    nums = numbersVar.get()
    chars = lettersVar.get()
    syms = symbolsVar.get()

    if(length <= 0):
        return messagebox.showerror("Length Error" ,"Password must be at least 1 character long.")
    if(not nums and not chars and not syms):
        return messagebox.showerror("Character Type Error" ,"You must select at least one character type.")

    messagebox.showinfo("Password", passwordGenerator(length, charType(nums, chars, syms)))

page = tk.Tk()
page.title("Random Password Generator")
passLength = tk.IntVar()
lettersVar = tk.BooleanVar()
numbersVar = tk.BooleanVar()
symbolsVar = tk.BooleanVar()
tk.Label(page, text='Password Length').grid(row = 0, pady = 5)
e1 = tk.Entry(page, textvariable = passLength).grid(row = 0, column = 1)
tk.Checkbutton(page, text='Letters', variable=lettersVar).grid(row = 1, column = 0, pady = 5)
tk.Checkbutton(page, text='Numbers', variable=numbersVar).grid(row = 1, column = 1)
tk.Checkbutton(page, text='Symbols', variable=symbolsVar).grid(row = 1, column = 2)
button = tk.Button(page, text="Generate Password", command=randomPasswordGenerator).grid(row = 2, column = 1)
page.mainloop()