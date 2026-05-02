def rotateFunction(nums):
    n=len(nums)
    f=0
    res=0
    num_sum=0

    for i in range(n):
        num_sum+=nums[i]

    for i in range(n):
        f+=i*nums[i]
    
    res=f

    for i in range(n-1,0,-1):
        f=f+num_sum-4*nums[i]
        res=max(res,f)

    
    return res

nums=list(map(int,input("Enter array: ").split()))
print(rotateFunction(nums))