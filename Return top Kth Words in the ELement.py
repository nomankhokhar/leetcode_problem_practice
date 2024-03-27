def topKFrequent( words, k):
    freq = {}
    topKthElement = ['' for i in range(len(words) + 1)]
    for i in range(len(words)):
        freq[words[i]] = 1 + freq.get(words[i], 0)
    for i in freq.items():
        topKthElement[i[1]] = i[0] 
    topElement = []
    for i in range(len(topKthElement) - 1, -1, -1):
        if topKthElement[i] == '':
            continue
        else:
            topElement.append(topKthElement[i])
        if len(topElement) == k:
            break
    return topElement
        
words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems"]
k = 2
print(topKFrequent(words, k))