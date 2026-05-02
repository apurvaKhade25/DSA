def duplicate(arr):
    seen={}
    for i in range(len(arr)):
        seen[arr[i]]=seen.get(arr[i],0)+1
    
    for key in seen:
        if seen[key]>1:
            return True

    return False

arr=[3,3,3,3,5,5,2]
print(duplicate(arr))
arr=[3,5,6,4,7]
print(duplicate(arr))
arr=[]
print(duplicate(arr))
