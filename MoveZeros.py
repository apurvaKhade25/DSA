def moveZero(nums):
    l=0
    for r in range(len(nums)):
        if nums[r]:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
    return nums
    
nums=list(map(int,input("Enter array: ").split()))
print(moveZero(nums))
