def water(arr):
    max_A=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            height=min(arr[i],arr[j])
            width=j-i
            area=width*height
            max_A=max(area,max_A)
    
    return max_A

# arr=list(map(int,input("Enter array: ").split()))
arr=[1,8,6,2,5,4,8,3,7]
print(water(arr))