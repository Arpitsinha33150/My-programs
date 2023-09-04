import random
chars='1','2','3','4','5','6','7','8','9','10'
a=int(input("Enter the number of rounds: "))
counter=0
Score=0
for k in range(a):
    counter=counter+1
    print("Round number",counter,":")
    b=int(random.choice(chars))
    n=int(input("Guess the number: "))
    if n==b:
        Score=Score+1
        print("+1")
    else:
        Score=Score-1
        print("-1") 
print(" ")
print("YOUR SCORE WAS",Score)        
if Score==a:
    print("CONGO YOU WON")
else:
    print("OOPS.. YOU LOST BETTER LUCK NEXT TIME")                