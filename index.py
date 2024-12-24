import random

print("Following are the Rules of the Game: \n 1. Rock vs Paper -> Paper Wins \n 2. Rock vs Scissors -> Rock Wins \n 3. Paper vs Scissors -> Scissors Wins")
print ("Enter 1 for Rock , 2 for Paper and 3 for Scissors")
print ("The side with three Wins will be the winner")

userScore = 0
computerScore = 0

while userScore < 3 and computerScore < 3 :
    userChoice = int(input("Enter your choice now:"))
    if userChoice !=1 and userChoice !=2 and userChoice !=3:
        print("Invalid Choice")
        exit()
    else:
        computerChoice = random.randint(1,3)
        if computerChoice == 1 and userChoice == 1:
            print("Computer choose Rock and You Choose Rock, its a Tie \n No one gets a point")
        elif computerChoice == 2 and userChoice == 1:
            print("computer choose Paper and you choose Rock, Computer gets a point")
            computerScore +=1
        elif computerChoice == 3 and userChoice ==1:
            print("Computer choose scissors and you choose Rock , you get a point")
            userScore +=1
        if computerChoice == 1 and userChoice == 2:
            print("Computer choose Rock and You Choose paper, you get a point")
            userScore +=1
        elif computerChoice == 2 and userChoice == 2:
            print("computer choose Paper and you choose paper, Its a Tie. No one gets a point")
        elif computerChoice == 3 and userChoice ==2:
            print("Computer choose scissors and you choose paper , Computer gets a point")
            computerScore +=1
        if computerChoice == 1 and userChoice == 3:
            print("Computer choose Rock and You Choose scissors, compuer gets a point")
            computerScore +=1
        elif computerChoice == 2 and userChoice == 3:
            print("computer choose Paper and you choose Scissors, You get a point")
            userScore +=1
        elif computerChoice == 3 and userChoice ==3:
            print("Computer choose scissors and you choose Scissors , Its a Tie. No one gets a point")
        else:
            print("")
print("C omputer's Final Scors are: ", computerScore)
print( "Your Final Score are: ", userScore)
if computerScore > userScore:
    print("Computer Wins")
else:
    print(" \n You Win")

    