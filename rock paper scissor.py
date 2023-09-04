import random

rounds = int(input("Enter the number of rounds: "))
options = ('ROCK', 'SCISSOR', 'PAPER')

user_score = 0
computer_score = 0

def Rule(computer, user):
    global user_score, computer_score

    if user == "ROCK":
        if computer == 'PAPER':
            computer_score += 1
            user_score -= 1
            print("You lost (-1)")
        elif computer == 'SCISSOR':
            computer_score -= 1
            user_score += 1
            print("You won (+1)")
        else:
            print("It is a draw (+0 [TO BOTH])")
    elif user == "SCISSOR":
        if computer == 'PAPER':
            computer_score -= 1
            user_score += 1
            print("You won (+1)")
        elif computer == 'ROCK':
            computer_score += 1
            user_score -= 1
            print("You lost (-1)")
        else:
            print("It is a draw (+0 [TO BOTH])")
    elif user == "PAPER":
        if computer == 'ROCK':
            computer_score -= 1
            user_score += 1
            print("You won (+1)")
        elif computer == 'SCISSOR':
            computer_score += 1
            user_score -= 1
            print("You lost (-1)")
        else:
            print("It is a draw (+0 [TO BOTH])")

print("")

for k in range(rounds):
    print(" ")
    print("Round number", k + 1, ":-")
    user = input("Type 'ROCK', 'SCISSOR', 'PAPER': ").upper()
    computer = random.choice(options)
    print(computer)

    if user not in options:
        print("PLEASE ENTER A VALID CHOICE NEXT TIME")
        quit()
    else:
        Rule(computer, user)

user_score = max(user_score, 0)
computer_score = max(computer_score, 0)

print("Final Scores:")
print("User Score:", user_score)
print("Computer Score:", computer_score)
