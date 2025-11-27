#last print statement will print whether number is found in the tuple or not.

tup=(1,2,3,45,5,6,7,8)
x=int(input("enter the number:"))
for num in tup:
    if num == x:
        print("num found",x)
        break
    print(num)
print("end")