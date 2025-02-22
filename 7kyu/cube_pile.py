# https://www.codewars.com/kata/5592e3bd57b64d00f3000047

def find_nb(m):
    i = 0
    while m >= 1:
        m -= i**3
        i += 1
    if m == 0:
        return i-1
    else:
        return -1

print(find_nb(4183059834009))