import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 
           'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 
           'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Pypassword generator:)\n")
letter_amount = int(input("How many letters would you like in your password?\n"))
symbol_amount = int(input("How many symbols would you like?\n"))
number_amount = int(input("How many numbers would you like?\n"))

password_list = []                           #make the vairable empyt so you can fill the list with what the client wants
for char in range(0, letter_amount):    #these for loops go through the 3 lists and pick the amount randomly
    password_list += random.choice(letters)
    
for char in range(0, symbol_amount):
     password_list += random.choice(symbols)

for char in range(0, number_amount):
     password_list += random.choice(numbers)

random.shuffle(password_list)    #this shuffles the password and keeps it random


password = ""               #this for loops turn the shuffled list back into a string to print to the prompt
for char in password_list:
     password += char

print(f"Your password is: {password}")