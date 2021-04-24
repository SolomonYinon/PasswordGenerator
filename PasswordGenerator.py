from tkinter import *
import random

NumbersIn = False
UpperIn = False
LowerIn = False
SpecialIn = False

Lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
Numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SpecialDigits = [' ' ,'!' , '"' , '#' , '$' , '%' , '&' , "'" , '(' , ')' , '*' , '+' , ',' , '-' , '.' , '/' , ':' , ';' , '<' , '=' , '>' , '?' , '@' , '[' , "\\" , "]" , '^' , "_" , "`" , "{" , "|" , "}" , "~"]
root = Tk()
root.title("Passord Generator")


LabelDigits = Label(root , text = "Please enter how many digits the password is:")
LabelDigits.grid(row = 1 , column = 0)
PasswordLabel = Label(root , text = "Your password is:")
GeneratedPassword = Entry(root , width = 20)
Input = Entry(root , width = 20)
Input.grid(row = 2 , column = 0)
PasswordLabel.grid(row = 1 , column = 1)
GeneratedPassword.grid(row = 2 , column = 1)

def lengthOfPassword():
    global DigitsNum
    global Numbers
    global Lowercase
    global Uppercase
    global SpecialDigits
    global root
    AllDigits = []
    DigitsNum = Input.get()
    if NumbersIn is True:
        AllDigits += Numbers
    if LowerIn is True:
        AllDigits += Lowercase
    if UpperIn is True:
        AllDigits += Uppercase
    if SpecialIn is True:
        AllDigits += SpecialDigits
    password = ""
    for i in range(int(DigitsNum)):
        password += random.choice(AllDigits)
    GeneratedPassword.delete(0 , END)    
    GeneratedPassword.insert(0 , password)
    
def isNumbers():
    global NumbersIn
    NumbersIn = not NumbersIn
    ButtonNumbers = Button(root , text = "Numbers" , padx = 10 , pady = 10 , command = isNumbers)
    
def isLower():
    global  LowerIn
    LowerIn = not LowerIn

def isUpper():
    global UpperIn
    UpperIn = not UpperIn
    
def isSpecial():
    global SpecialIn
    SpecialIn = not SpecialIn

ButtonYes = Button(root , text = "Yes!" , padx = 10 , pady = 10 , command = lengthOfPassword)
ButtonNumbers = Button(root , text = "Numbers" , padx = 10 , pady = 10 , command = isNumbers)
ButtonLowercase = Button(root , text = "Lowercase" , padx = 10 , pady = 10 , command = isLower)
ButtonUppercase = Button(root , text = "Uppercase" , padx = 10 , pady = 10 , command = isUpper)
ButtonSpecial = Button(root , text = "Special Digits" , padx = 10 , pady = 10 , command = isSpecial)
ButtonYes.grid(row = 4 , column = 1)
ButtonNumbers.grid(row = 3 , column = 0)
ButtonLowercase.grid(row = 4 , column = 0)
ButtonUppercase.grid(row = 5 , column = 0)
ButtonSpecial.grid(row = 6 , column = 0)

root.mainloop()
