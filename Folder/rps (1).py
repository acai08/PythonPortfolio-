#Annie
#Rock Paper Scissors
#A simulation of the popular rock paper scissors game where the player plays agaisnt the computer


#Initial
import random
score = 0
computer = 0

#Functions
def rsp():
    global score
    global computer
    print("Welcome to Rock Paper Scissors!")
    while True:
        choose = input("What do you want to play? Choose rock, paper, or scissors: ")
        computer = random.randint(1,3)
        if computer == 1 and choose == "rock":
            print ("The computer chooses rock.")
            print ("You are tied!")
            score = score + 0
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 1 and choose == "paper":
            print ("The computer chooses rock.")
            print ("You Win!")
            score = score + 1
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 1 and choose == "scissors":
            print ("The computer chooses rock.")
            print ("You Loose!")
            score = score + 0
            computer = computer + 1
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 2 and choose == "rock":
            print ("The computer chooses paper.")
            print ("You Loose!")
            score = score + 0
            computer = computer + 1
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 2 and choose == "paper":
            print ("The computer chooses paper.")
            print ("You are Tied!")
            score = score + 0
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 2 and choose == "scissors":
            print ("The computer chooses paper.")
            print ("You Win!")
            score = score + 1
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 3 and choose == "rock":
            print ("The computer chooses scissors.")
            print ("You are Tied!")
            score = score + 0
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 3 and choose == "paper":
            print ("The computer chooses scissors.")
            print ("You Loose!")
            score = score + 0
            computer = computer + 1
            print(f"player score:{score} and computer score: {computer}")

        elif computer == 3 and choose == "scissors":
            print ("The computer chooses scissors.")
            print ("You Win!")
            score = score + 1
            computer = computer + 0
            print(f"player score:{score} and computer score: {computer}")

        game = input ("Do you want to play again? (yes or no): ")
        if game == "yes":
            return rsp()

        else:
            break

#Main
rsp()
