def Furthest_house(nums):
    n=len(nums)
    max_dist=0

    # backward loop
    for i in range(n-1,-1,-1):
        if nums[i]!=nums[0]:
            max_dist=max(max_dist,i)

    # forward loop
    for i in range(n):
        if nums[i]!=nums[n-1]:
            max_dist=max(max_dist,(n-1)-i)
    
    return max_dist


nums=[4,4,4,11,4,4,11,4,4,4,4,4]
print(Furthest_house(nums))