def twoEdits(dict,queries):
    res=[]
    for word in dict:
        if word in queries:
            res.append(word)
    return res

queries = ["word","note","ants","wood"]
dict= ["wood","joke","moat"]
print(twoEdits(queries,dict))
        