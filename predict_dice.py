#Hangman Dice game
import random 
a = int(input("Enter the number of dice you want to roll: "))
b= int(input("Enter the sum You want predict for the dice rolls: "))
total = 0
for i in range(a):
    r = random.randint(1, 6)
    
    total  = total + r
    
    print("The number on the dice are:",r)
print("The sum of all",a,"dice are: ",total)
if total==b:
        print("Congratulations your predicted num is same")
else:
        print("Oops Sorry your prdicted number is not same")


    





