def firstUnique(s):
    seen={}
    
    for i in s:
        seen[i]=seen.get(i,0)+1
    
    for i in range(len(s)):
        if seen[s[i]]== 1:
            return i
    
    return -1


s="leetcode"
print(firstUnique(s))

s="notebookpen"
print(firstUnique(s))