def binary(list,key):
    low = 0
    high = len(list)-1
    Found = False
    while low<=high and not Found:
        mid = (low+high)//2
        if key==list[mid]:
            Found = True
        elif key>list[mid]:
            low = mid+1
        else:
            high = mid+1
    if Found == True:
        print("key is founded")
        print(list.index(key))
    else:
        print("key was not founded")    
num = int(input("Enter the list length: "))
print("Enter the numbers in your list: ")
list = [int(input()) for i in range(num)]
list.sort()
print(" ")
key = int(input("Enter the key: "))
binary(list, key)