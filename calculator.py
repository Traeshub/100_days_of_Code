logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''
print(logo)
operators ='''
+
-
*
/'''

number = float(input("What's the first number?:"))
print(operators)
operation = input("Pick an operation:")
nxt_num = float(input("What is the next number?:"))

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

functions = {"+ ": add, "-": sub, "*": mult, "%": div}

def calculations(n1, n2):
    if operation == "+":
        answer = functions["+ "](number, nxt_num)
        print(f"Answer is: {answer}")
        return answer
    elif operation == "-":
         answer = functions["-"](number, nxt_num)
         print(f"Answer is: {answer}")
         return answer
    elif operation == "*":
         answer = functions["*"](number, nxt_num)
         print(f"Answer is: {answer}")
         return answer
    else:
         answer = functions["/"](number, nxt_num)
         print(f"Answer is: {answer}")
         return answer
    

cont_calc = True
while cont_calc:
    calculations(number, nxt_num)
    con_calculating = input(f"Would you like to continue calculating?:\n").lower()
    if con_calculating == "no":
        cont_calc = False
    else:
        num_3 = float(input("What is the next number?:"))
        print(operators)
        nxt_operation =  input("Pick an operation:")
        calculations()

        # calculation continuation still in progress