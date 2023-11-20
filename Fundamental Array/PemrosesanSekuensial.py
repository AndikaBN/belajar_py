var_array = [1,2,3,4,5]

for i in range(len(var_array)):
    curent_element = var_array[i]
    next_index =i+1

    if next_index < len(var_array):
        next_element = var_array[next_index]
    else:
        next_element = None
    
    print(f"Current element: {curent_element}, next elements: {next_element}")

var_arr = [1, 7, 2, 89, 3]
left_pointer = var_arr[0]

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)
