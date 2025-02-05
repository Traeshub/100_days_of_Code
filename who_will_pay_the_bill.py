friends = ["alice", "bob", "charlie", "david", "emanuel"]

import random
whos_paying = random.randint(0,4)   #randint function picks through a set of picked numbers excluding the last number(5)

if whos_paying == 0:
    print("alice is paying!")
elif whos_paying == 1:
    print("bob is paying!")
elif whos_paying == 2:
    print("charlie is paying!")
elif whos_paying == 3:
    print("david is paying!")
else:
    print("emmanuel is paying!")    #can also use random.choice function