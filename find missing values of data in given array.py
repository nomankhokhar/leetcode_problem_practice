def findDisappearedNumbers(nums):
    largNumber = nums[0]
    for i in range(len(nums)):
        if largNumber < nums[i]:
            largNumber = nums[i]
        
    indexOfNumber = [""  for i in range(largNumber)]
    dic = {}
    for i in range(len(nums)):
        dic[nums[i]] = 1 + dic.get(nums[i], 0)
    
    for i in dic.items():
        indexOfNumber[i[0]-1] = i[0]
    missingValue = []    
    for i in range(len(indexOfNumber)):
        if indexOfNumber[i] == "":
            missingValue.append(i + 1)
    print(missingValue)

    
nums = [4,5,2,6,8,2,1,5]
findDisappearedNumbers(nums)