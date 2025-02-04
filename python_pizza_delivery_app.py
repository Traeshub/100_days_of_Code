print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?\n")
pepperoni = input("Do you want peppperoni on your pizza? Y or N?:\n")
extra_cheese = input("Do you want extra cheese on your pizza? Y or No?:\n")
price = 0 
#add a variable for the ending result as zero so it can change

if size == "S":
    price = 15
elif size == "M":
    price = 20
else:
    price = 25

if pepperoni == "Y":
    if size == "S":
        price += 2
    else:
        price += 3

if extra_cheese == "Y":
    price += 1
print(f"Your total price is ${price}")