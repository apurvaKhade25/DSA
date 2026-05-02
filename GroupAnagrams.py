def groupAna(arr):
    hashset={}

    for word in arr:
        key=" ".join(sorted(word))
        print(key)

        if key in hashset:
            hashset[key].append(word)
        else:
            hashset[key]=[word]

        # hashset[key].append(word)
        # print(hashset)

    return list(hashset.values())


arr=["eat","tea","tan","ate","nat","bat"]
print(groupAna(arr))

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

