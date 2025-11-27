tup=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number:"))
indx=0
for num in tup:
    if num==x:
        print("number is found at index",indx)
        break
    indx+=1

else:
    print("number is not found in the tuple")    