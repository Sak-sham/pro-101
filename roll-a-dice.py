import random
no=random.randint(1,6)
response=input("Do you want to roll the dice?")
while response== "y":
    if no == 1: print("[-----]","[ ]","[ 0 ]", "[ ]", "[-----]")
    if no == 2: print("[-----]","[ ]","[ 0 0]", "[ ]", "[-----]")
    if no == 3: print("[-----]","[ ]","[ 0 0 0]", "[ ]", "[-----]")
    if no == 4: print("[-----]","[ ]","[ 0 0 0 0]", "[ ]", "[-----]")
    if no == 5: print("[-----]","[ ]","[ 0 0 0 0 0]", "[ ]", "[-----]")
    if no == 6: print("[-----]","[ ]","[ 0 0 0 0 0 0]", "[ ]", "[-----]")

if response =='n':
    print("exited")
