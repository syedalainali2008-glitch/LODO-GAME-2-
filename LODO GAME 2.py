import random
dice1=random.randint(1,6)
dice2=random.randrange(1,7)
enter=str(input("ENTER THROW :"))
if enter=="THROW":
    for i in range(1,6,1):
        print("PROCESSING....")
    print("THIS IS YOUR FIRST DICE:",dice1)
    print("THIS IS YOUR SECOND DICE:",dice2)
    sum=(dice1+dice2)
    print("NOW THIS IS HOW MUCH YOU  MOVE FORWARD:",sum)
