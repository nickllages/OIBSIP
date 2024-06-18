import random as rng

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
def charType():
    nums = ""
    chars = ""
    syms = ""

    while(nums.lower() != 'y' and nums.lower() != 'n'):
        nums = input("Would you like numbers in your password? (Y/N)\n")
    while(chars.lower() != 'y' and chars.lower() != 'n'):
        chars = input("Would you like letters in your password? (Y/N)\n")
    while(syms.lower() != 'y' and syms.lower() != 'n'):
        syms = input("Would you like symbols in your password? (Y/N)\n")

    if(nums == 'y'):
        if(chars == 'y'):
            if(syms == 'y'):
                return "all"
            else:
                return "alnum"
        elif(syms == 'y'):
            return "ns"
        else:
            return "num"
    
    elif(chars == 'y'):
        if(syms == 'y'):
            return "ls"
        else:
            return "alpha"
    
    elif(syms == 'y'):
        return "symbol"
    
    else:
        print("You must select at leat one character type for this password.")
        return charType()


# Allows user to choose length of password
def length():
    return int(input("How many character do you want in your password?\n"))

# Runs the command line password generator
def randomPasswordGenerator():
    print("Hello, Welcome to the Random Passowrd Generator! Let's create a random password!")
    print("Your password is: ", passwordGenerator(length(), charType()))

randomPasswordGenerator()