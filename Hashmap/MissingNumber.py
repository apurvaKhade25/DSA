def MissingNumber(arr):
    nums=set(arr)

    for i in range(len(arr)+1):
        if i not in nums:
            return i 
        
arr=[1,3,9]
print(MissingNumber(arr))
