# with string reverse
def reverse_int(x:int) -> int:
    x_str = str(x)
    if x_str[0] == '-':
         reversed_int = '-' + x_str[:0:-1]
    else:    
        reversed_int = str(x)[::-1]
    
    return int(reversed_int)


def reverse(x: int) -> int: 
    result = 0
    x_remaining = abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10 # 3
        x_remaining //= 10 
    return -result if x < 0 else result 

print(reverse(-123))

