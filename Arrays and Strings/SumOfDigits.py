def sum_of_digits(x):
    x=abs(x)
    total=0

    while x>0:
        total+=x%10
        x//=10
    
    return total
            
def total(arr):
    for i in range(len(arr)):
        if arr[i]<0:
            arr[i]+=i
        else:
            arr[i]=sum_of_digits(arr[i])
    return arr


n=int(input("Enter number: "))
arr=[]
for i in range(n):
    elem=int(input(f"Enter input {i+1}: "))
    arr.append(elem)

print(total(arr))


