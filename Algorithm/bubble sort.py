#input_lis = [7, 4, 5, 1, 3]
input_lis = [4, 2, 6, 7, 2, 9, 8]


def bubble_sort (input):
    
    for i in range(len(input)-1):
        #print(i, i+1)
        for j in range(len(input) -i -1):  # -i
            print(i)  
            print(j, j+1)
            if input[j] > input[j+1]:
                input[j], input[j+1] = input[j+1], input[j]
            else: 
                pass
        

    output = input
    return output

print(bubble_sort(input_lis))


# 0,1    1,2     2,3    3,4 break