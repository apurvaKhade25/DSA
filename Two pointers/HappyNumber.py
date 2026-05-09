def happyNum(num):
    seen=set()
    while (num!=1):
        if num in seen:
            return False
        seen.add(num)
        total=0

        while num>0:
            last_digit=num%10
            total+=last_digit*last_digit
            num=num//10
        
        num=total
    
    return True

num=int(input("Num: "))
print(happyNum(num))

# o(logn)