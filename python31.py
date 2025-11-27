tup=(1,2,3,45,5,6,7,8)
x=int(input("enter the number:"))
for num in tup:
    if num == x:
        print("num found",x)
        break
    print(num)
else:
    print("end")
#else doent execute here if the number is found in the given tuple.
