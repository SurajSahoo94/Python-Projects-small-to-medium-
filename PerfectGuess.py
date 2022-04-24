import random

random_num =  random.randint(1,50)

#print(random_num)
guesses = 0
user_guess = None #The None keyword is used to define a null value, or no value at all.

while user_guess != random_num:
    guesses +=1
    user_guess = int(input("Enter your number between 1-50\n"))
    if (user_guess == random_num):
        print("Your guess is right! No.of attempts you took is",guesses)
        
    if user_guess > random_num:
        print("Lower number please")
    elif user_guess < random_num:
        print("Higher number please")
        
 
  
    
    