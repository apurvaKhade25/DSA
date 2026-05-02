def circularArr(arr,target,start):
    n=len(arr)
    mindist=float('inf')
    for i in range(n):
        if arr[i]==target:
            d=abs(i-start)                          ## left
            circular=n-d                                   ## right 
            mindist=min(mindist,d,circular)
    return mindist if mindist!=float('inf') else -1


arr=input("Enter array: ").split()
target=input("Enter target: ")
start=int(input("Enter start index: "))
print(circularArr(arr,target,start))