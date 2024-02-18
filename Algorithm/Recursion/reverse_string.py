# my solution
def reverseString(str):
    
    lis = []
    for i in range(len(str)):
        lis.append(str[len(str)-1-i])
        
    return ''.join(lis)
    

def reverseStringRecursive(str):
    # Base case: if the string is empty or consists of a single character, it is its own reverse.
    if len(str) <= 1:
        return str
    else:
        # Recursive step: reverse the substring excluding the first character,
        # then append the first character to the end of this reversed substring.
        # repeat same process without the last element.(first character before)
        return reverseString(str[1:]) + str[0]
    
    
    

str = 'earth'


# print(reverseString(str))

print(reverseString(str))

print(reverseStringRecursive(str))
