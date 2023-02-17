# use randon number
import random
randNumber = random.randint(1,100)
# print(randNumber)

userGuess = None
guesses = 0
while(userGuess != randNumber):
    userGuess = int(input("Enter your guess:"))
    guesses += 1
    if(userGuess == randNumber):
        print("your guess is right")
    else:
        if (userGuess>randNumber):
            print("The guess is Wrong ! enter a smaller NUmber .:")
        else:
            print("the guess is wrong! enter a larger number.:")
  
# print(f"you guessed the number in {guesses} guesses")
# with open("highScore.txt","r") as f:
#     highScore = int(f.read())

# if(guesses<highScore):
#     print("you just broken the highscore")
#     with open("highScore.txt","w") as f:
#         f.write(str(guesses))