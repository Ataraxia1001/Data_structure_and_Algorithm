# Google Question. Search for first recurring array.


# my solution.
arr1 = [2,5,1,2,3,5,1,2,4]
arr2 = [2,1,1,2,3,5,1,2,4]
arr3 = [2,3,4,5]
arr4 = [2,5,1,2,3,5,1,2,4]

def first_recurring_char(arr): # O(n)
    if list(set(arr)) == arr:
        return None
    else: 
        lis = []
        for v in arr:
            if v in lis:
                return v
            else:
                pass
            lis.append(v)
            
            
def first_recurring_char2(arr): # O(n)
    if list(set(arr)) == arr:
        return None
    else: 
        for i, v in enumerate(arr):
            if v in arr[i+1:]:
                return v
            
            
# print(first_recurring_char2(arr1))
# print(first_recurring_char2(arr2))
# print(first_recurring_char2(arr3))
print(first_recurring_char([2,5,1,2,3,5,1,2,4]))
print(first_recurring_char2([2,5,5,2,3,5,1,2,4]))
# print(arr3)
# print(list(set(arr3)))