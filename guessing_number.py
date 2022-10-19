import random
num = random.randint(1,9)
guess = None

while guess != num:
    guess = int(input("guesss a number between 1 to 9: "))
    if guess < num:
        print("sorry, guess is tooo low try again!")
    elif guess > num:
        print("sorry, guess is tooo high try again!")
    elif guess == num:
        print("YOU WON!")
        exit(0)
        
        OUTPUT:
          guesss a number between 1 to 9: 5
          sorry, guess is tooo high try again!
          guesss a number between 1 to 9: 3   
          sorry, guess is tooo low try again!
          guesss a number between 1 to 9: 4  
          YOU WON!
