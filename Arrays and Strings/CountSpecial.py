def SpecialChars(arr):
    word=set(arr)
    special=set()

    for i in word:
        if i.upper() in word and i.lower() in word:
            special.add(i.upper())
    
    print(list(special))
    return len(special)


arr="HeLLoLLooEEOO"
print(SpecialChars(arr))