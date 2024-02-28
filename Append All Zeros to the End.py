
def move_zeros_to_end(arr):
    left = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[left], arr[i] = arr[i], arr[left]
            left += 1
    return arr

def move_zeros_to_end_2nd(arr):
    index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[index] = arr[i]
            index = index + 1
    for count in range(index , len(arr)):
        arr[count] = 0
    return arr
input_array = [0, 0, 1, 0, -2, 8, 0, 4]

result = move_zeros_to_end(input_array)
result2 = move_zeros_to_end_2nd(input_array)

print(result)
print(result2)

