# Reeborg's World game

def turn_left():
    turning = "turn left"
def at_goal():
    goal = "at goal"
def right_is_clear():
    right = "is clear"
def front_is_clear():
    front = "is clear"
def move():
    move = "move"

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear:
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear:
        move()
    else:
        turn_left()