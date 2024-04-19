import random
 
    #initiate a secret number
secret_number=random.randint(1,100)
print(secret_number)
    #user input - to guess what is the number from user
userguessing= int(input("Enter Number:"))
    #check the answer is correct
if userguessing == secret_number:
    print("Bingo!")
    #give hint, is the guess number is too high
elif userguessing > secret_number:
    print("too low")
else:
    print("you loss")