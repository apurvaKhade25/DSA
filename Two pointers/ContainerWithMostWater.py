def water(height):
    # max_A=0
    # for i in range(len(arr)):
    #     for j in range(i+1,len(arr)):
    #         height=min(arr[i],arr[j])
    #         width=j-i
    #         area=width*height
    #         max_A=max(area,max_A)
    
    # return max_A

    max_a=0
    left=0
    right=len(height)-1

    while left<=right:
            width=right-left
            h=min(height[left],height[right])
            area=width*h
            max_a=max(area,max_a)

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

    return max_a

# arr=list(map(int,input("Enter array: ").split()))
arr=[1,8,6,2,5,4,8,3,7]
print(water(arr))