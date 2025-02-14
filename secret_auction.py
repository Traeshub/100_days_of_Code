
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\
'''
print(logo)
print("Welcome to the secret Auction.\n")
users_info = {}
another_user = True

def highest_bid(bid_dictionary):
    winner = ""
    highest_bidder = 0
    
    for bidder in bid_dictionary:
        bid_amount = bid_dictionary[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with ${highest_bidder}")

while another_user:
    user_name = input("What is your name?\n")
    users_bid = int(input("What will be your bid?: \n$"))
    next_user = input("Are there any other users that want to bid?\n")
    users_info [user_name] = users_bid
    if next_user == "yes".lower():
        print("\n" * 60)
    else:
        another_user = False
        highest_bid(users_info)