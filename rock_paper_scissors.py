rock = '''
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
       '''

paper = '''
       /')    ./')
      /' /.--''./'')
 :--''  ;    ''./'')
 :     '     ''./')
 :           ''./'
 :--''-..--''''''
'''

scissors = '''
.-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / /
  '''

import random
choices = [rock, paper, scissors]
choice = int(input("What do you chose? type 0 for rock, 1 for paper or 2 for scissors.\n"))
if choice >= 0 and choice <= 2:
    print(choices[choice])

computers_choice = random.randint(0,2)
print(f"Computer chose: {computers_choice} ")
print(choices[computers_choice])


if choice == 0 and computers_choice == 0:
    print("its a tie")
elif choice == 1 and computers_choice == 0:
    print("You win!")
elif choice == 2 and computers_choice == 0:
    print("You lose")

if choice == 0 and computers_choice == 1:
    print("You lose!")
elif choice == 1 and computers_choice == 1:
    print("its a tie")
elif choice == 2 and computers_choice == 1:
    print("You win!")

if choice == 0 and computers_choice == 2:
    print("You win!")
elif choice == 1 and computers_choice == 2:
    print("You lose!")
elif choice == 2 and computers_choice == 2:
    print("its a tie")