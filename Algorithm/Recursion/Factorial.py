
def findFactorialRecursive(num):  # O(n)
    if num == 1:
        return 1
    return num * findFactorialRecursive(num-1)


def findFactorialIterative(num): # O(n)
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result
    

print(findFactorialRecursive(5))
print(findFactorialIterative(0))