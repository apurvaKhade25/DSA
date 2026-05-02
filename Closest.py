##3488
from bisect import bisect_left
from collections import defaultdict

def closest(nums,queries):
    n=len(nums)
    mp=defaultdict(list)

    for i in range(n):
        mp[nums[i]].append(i)
    
    ans=[]

    for q in queries:
        positions=mp[nums[q]]
        print(positions)

        if len(positions)==1:
            ans.append(-1)
            continue

        pos=bisect_left(positions,q)
        res=float('inf')

        left=positions[(pos-1)%len(positions)]
        d1=abs(left-q)
        res=min(res,d1,n-d1)

        right=positions[(pos+1)%len(positions)]
        d2=abs(right-q)
        res=min(res,d2,n-d2)
    
        ans.append(res)
    
    return ans


nums = [1,3,1,4,1,3,2]
queries =[0,3,5]
print(closest(nums,queries))




        
    