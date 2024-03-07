arr = [1,1,1,2,2,3]

def topKthElement(data, k):
    count = {}
    freq = [[] for i in range(len(data) + 1)]
    
    for i in range(len(arr)):
        count[arr[i]] = 1 + count.get(arr[i] , 0)
    for n , c in count.items():
        freq[c].append(n)
    res = []
    for i in range(len(freq)-1 , 0 ,-1):
        for i in freq[i]:
            res.append(i)
            if len(res) == k:
                return res
    
print(topKthElement(arr, 1))
