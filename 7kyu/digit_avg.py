# https://www.codewars.com/kata/5a32526ae1ce0ec0f10000b2

import math

def digits_average(x):
    num = str(x)
    while len(num) > 1:
        new_num = []
        for i in range(len(num) - 1):
            avg = (int(num[i]) + int(num[i + 1])) / 2
            new_num.append(math.ceil(avg))

        num = ''.join(map(str, new_num))
    
    return int(num)

# Test with the input 246
print(digits_average(246))  # Output: 4
