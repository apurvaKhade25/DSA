def addDigits(num):            ##Add Digits: Only single digit valid
    num=abs(num)

    while num>=10:
        total=0

        while num>0:
            total+=num%10
            num//=10
        
        num=total

    return num
    
num=int(input("Enter number: "))
print(addDigits(num))
