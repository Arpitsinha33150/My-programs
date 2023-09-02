import random
chars='qwertyuiopasdfghjklzxcvbnm1234567890'
m=int(input("Enter your password length: "))
n=int(input("Enter the number of passwords to br generated: "))
print("The passwords are:-")
for pwd in range(n):
    passwords=''
    for c in range(m):
        passwords += random.choice(chars)
    print(passwords)
a=int(input("Enter any number and press enter to exit "))
print(a)    