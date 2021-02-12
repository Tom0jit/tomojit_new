import random
min= 1
max= 6
roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    ran= random.randint(min, max)
    print (ran)
    if ran%2==0:
        print ("You can go ahead.")
        roll_again = input("Roll the dices again?")

    else :
        print ("No more moves.")
        break
