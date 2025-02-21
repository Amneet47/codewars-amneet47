# https://www.codewars.com/kata/56e7d40129035aed6c000632

def easyline(n):
    ini = [1]
    for i in range(n):
        left = ini + [0]
        right = [0] + ini
        current = [x + y for x, y in zip(left, right)]
        ini = current
        i += 1
    for j in range(len(ini)):
        ini[j] *= ini[j]
    return sum(ini)

print(easyline(7))
        
        