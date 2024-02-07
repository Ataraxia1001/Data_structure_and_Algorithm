#input_lis = [9, 6, 7, 3, 5]
input_lis = [4, 2, 6, 7, 9, 8]
#print(input_lis[2:])


# def search_min(input):
#     min_val = 0
    
#     for i in range(len(input)):
#         for j in range(i):
#             #print(i, j)
#             if input[i] <= input[j]:
#                 min_val = input[i]
#             else:
#                 min_val = input[j]
    
#     min_index = 0
#     for i in range(len(input)):
#         if input[i] == min_val:
#             min_index = i
    
#     return min_index, min_val


def find_minimum(input_list):
    if len(input_list) == 0:
        return None

    min_value = input_list[0]
    for element in input_list:
        if element < min_value:
            min_value = element
            
    min_index = 0
    for i in range(len(input_list)):
        if input_list[i] == min_value:
            min_index = i

    return min_index, min_value



# print(find_minimum([4, 2, 6, 7, 9, 8]))

print('---start selection sort---')
print('input list:', input_lis)
def selection_sort (input):
    
    for i in range(len(input)-1):
        min_index, min_value = find_minimum(input[i+1:])
        print(input[i+1:])
        print(min_index+i+1, min_value)
        if input[min_index+i+1] < input[i]:
            input[i], input[min_index+i+1] = input[min_index+i+1], input[i]
        print('changed input list:', input)
        print('------------------')

    output = input
    return output

print(selection_sort(input_lis))