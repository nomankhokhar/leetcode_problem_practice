Input = ['a', 'a', 'b', 'c', 'c', 'c']

def compresArray(data):
    if len(data) == 0:
        return 0
    doc = {}
    for i in range(len(data)):
        doc[data[i]] = 1 + doc.get(data[i], 0)
        
    compressArr = []
    for k ,v in doc.items():
        if v == 1:
            compressArr.append(k)
        else:
            compressArr.append(k)
            compressArr.append(v)
    
    return compressArr


print(compresArray(Input))
# ['a', 2, 'b', 'c', 3]s