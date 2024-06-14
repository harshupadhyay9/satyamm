import random
n=int(input("Enter the number : "))
m=int(input("Enter th number : "))
num = random.randint(n, m)
print("Your guessing range is between",n,"and",m)
guess = None
    
while guess != num:
    guess = input("guess a number between given range : ")
    guess = int(guess)
    
    if guess == num:
        print("congratulations! you won!")
        break
    else:
        print("nope, sorry. try again!")
