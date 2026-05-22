def longestSequence(arr):
    length=0
    arr=set(arr)
    longest=0

    for ch in arr:
        if ch-1 not in arr:
            while(ch+length) in arr:
                length+=1
            longest=max(length,longest)
    
    return longest

arr=map(int,input().split())
print(longestSequence(arr))
