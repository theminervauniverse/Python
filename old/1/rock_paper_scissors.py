signs = ["Rock", "Paper", "Scissors"]
choose = int(input("What Do you Choose?,Type 0 for Rock,1 For Paper or 2 for Scissors\n"))
choice = signs[choose]
print(choice)
import random
choice_computer = random.choice(signs)
print(choice_computer)
if choice == choice_computer:
    print("its a Draw")
elif choice == "Rock":
    if choice_computer == "Scissors":
        print("Computer chose - Scissors \nRock Wins Against Scissors You WIN! ")
    else:
        print("Computer chose - Paper \nPaper wins against Rock ! You Lose go F*ck yourself")
elif choice == "Scissors":
    if choice_computer == "Paper":
        print("Computer chose - Paper \nScissors win against Paper ! you WIN")
    else:
        print("Computer chose - Rock \nRock smashes Scissors You Lose! go F*ck yourself")
elif choice == "Paper":
    if choice_computer == "Rock":
        print("Computer chose - Rock \nPaper wins Against Rock You Win!")
    else:
        print("Computer chose - Scissors \nScissors win Against Paper You Loose! go F*ck yourself")
