counter=1
Num=int(input("Enter the number: "))
E=Num*10+1
for k in range(Num,E,Num):
    print(Num,"x",counter,"= ",k)
    counter=counter+1
