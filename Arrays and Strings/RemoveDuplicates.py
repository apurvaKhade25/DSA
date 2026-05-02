def RemoveDuplicates(nums):
    if not nums:
        return 0
   
    i=0

    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            i+=1
            nums[i]=nums[j]

    print(nums)
    return i+1

nums=list(map(int,input("Enter array: ").split()))
print(RemoveDuplicates(nums))