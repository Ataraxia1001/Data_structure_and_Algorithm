def fibonacciRecursive(n):  # O(2^n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)
    
print(fibonacciRecursive(6))    


def fib(num):   # O(n)
    if num < 2:
        return num
    a = 0
    b = 1
    total = 0
    for i in range(num-1):
        total = a+b
        a = b
        b = total
    return total

print(fib(6))