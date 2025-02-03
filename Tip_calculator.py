print("Welcome to the tip calculator")
bill_amount = float(input("What was the total of the bill?\n $")) #the code coversion has to happen at the variable level
tip_amount = int(input("How much tip would you like to give?" + " " "10,12, or 15?\n"))
amount_of_people = int(input("How many people are splitting the bill?\n"))
amount_as_percent = tip_amount / 100
total_bill_amount = bill_amount * amount_as_percent
final_amount = bill_amount + total_bill_amount
bill_per_person = final_amount / amount_of_people
round(bill_per_person)
print(f"Each person should pay $ {bill_per_person}:")