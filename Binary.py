def binarySearch(arr,target):
    start=0
    end=len(arr)

    while start<=end:
        mid=(start+end)//2

        if target == arr[mid]:
            return f"The target is at: {mid+1}"
        elif target>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1

arr=(int,input("Enter array elements: ").split())
target=int(input("Enter target: "))
print(binarySearch(arr,target))
