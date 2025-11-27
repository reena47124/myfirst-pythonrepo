nums=(1,4,9,16,25,36,49,64,81,100)
x=int(input("enter the number:"))
indx=0
while indx<len(nums):
    if nums[indx]==x:
        print("number found at index:",indx)
        break
    indx+=1
else:
    print("number not found!!!")    

