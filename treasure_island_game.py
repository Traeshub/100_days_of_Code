print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")
direction = input("You are at a crossroad. Where do you want to go? left or right?\n").lower()


#You can put inputs inside of if statements to continue the program through choices.
if direction == "left":      
    choice = input("You are now at a lake. What do you want to do? swim or wait?\n").lower()  #input inside of if statement
    if choice == "swim":
        print("Attacked by trout. GAME OVER.")
    elif choice == "wait":
        door_choice = input("After waiting you look around and find a building." 
                            "You go into the building and you have 3 doors to choose from; red, blue or yellow \n").lower()
        if door_choice == "red":
            print("Eaten by beasts, GAME OVER.")
        elif door_choice == "blue":
            print("Burned by fire, GAME OVER.")
        elif door_choice == "yellow":
            print("YOU WIN!!!")
        else:
            print("You choose a door that does not exist. Game over.")  #this is foor if the user's input is not one of the options
else:
    print("You have fell into a hole. GAME OVER.")