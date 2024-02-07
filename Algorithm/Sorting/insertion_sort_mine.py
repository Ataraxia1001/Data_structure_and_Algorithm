numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
num2 = [5,9,3,10,45,2,0]

def insertionSort(lis):
    for i in range(len(lis)):
        #lis[i+1]
        for j in range(i):
            #print(f'i={i}, j={j}')
            if lis[i] < lis[j]:
                lis[i], lis[j] = lis[j], lis[i]
    return lis
            
print(insertionSort[numbers])
print(insertionSort(num2))

# It might perform more comparisons than necessary by starting from the beginning for each element rather than optimizing to start the comparison from the element's current position backwards. 
# Moreover, it lacks the optimization of "shifting" elements, which is more efficient than swapping when dealing with insertion operations in arrays or lists.