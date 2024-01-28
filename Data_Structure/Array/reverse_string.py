string = 'Hi My name is Andrei'

# both solutions are mine.
def reverse_string(string):
    reversed_lis = []
    for i in range(1, len(string)+1):
        reversed_lis.append(string[-i])
        
    return ''.join(str(x) for x in reversed_lis)

print(reverse_string(string))


def reverse_string2(string):
    str_lis = list(string)
    return ''.join(str_lis[-i] for i in range(1, len(str_lis)+1))

print(reverse_string2(string))