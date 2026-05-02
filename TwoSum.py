def twosum(arr,target):
    seen={}
    for i in range(len(arr)):
        diff=target-arr[i]
        if diff in seen:
            return seen[diff],i
        
        seen[arr[i]]=i
    return []

arr=[3,4,5,6,7,7,5]
target=11
print(twosum(arr,target))