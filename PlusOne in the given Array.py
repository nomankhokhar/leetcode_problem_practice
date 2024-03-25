def plusOne(digits):
    digits_into_str = ''.join(map(str, digits))
    
    incremented = str(int(digits_into_str) + 1)
    
    result = []
    for digit in incremented:
        result.append(int(digit))
    
    print(result)

num = [1, 9, 9]
plusOne(num)
