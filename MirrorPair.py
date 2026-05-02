def mirrorPair(nums):
    prev={}
    ans=float('inf')

    for i in range(len(nums)):
        if nums[i] in prev:
            ans=min(ans,i-prev[nums[i]])
        prev[int(str(nums[i])[::-1])]=i
    
    return -1 if ans==float('inf') else ans

nums =[12,21,45,33,54]
print(mirrorPair(nums))