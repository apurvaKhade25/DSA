def mergeAlternate(arr1,arr2):
    i=0
    j=0
    res=[]

    while(i<len(arr1) or  j<len(arr2)):
        if i<len(arr1):
            res.append(arr1[i])
            i+=1
        if j<len(arr2):
            res.append(arr2[j])
            j+=1
        
    return "".join(res)

arr1="abc"
arr2="pfbks"
print(mergeAlternate(arr1,arr2))
        