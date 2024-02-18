name = "The cat in the hat"

def reverceStringWithWordWise(names):
    sentence = ""
    words = []
    start = 0
    end = 0
    for i in names:
        end += 1
        if(i == " "):
            words.append(name[start:end - 1])
            start = end
    words.append(name[start:len(names)])
    
    for i in words:
        sentence += i[::-1]
        sentence += " "
    return sentence
  



print(reverceStringWithWordWise(name))