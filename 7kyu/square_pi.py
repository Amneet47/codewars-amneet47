# https://www.codewars.com/kata/5cd12646cf44af0020c727dd

import math
def square_pi(digits):
    pi = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    lst_pi = [int(digit) for digit in str(pi)[:digits]]
    for i in range(len(lst_pi)):
        lst_pi[i] *= lst_pi[i]
    s = sum(lst_pi)
    sq = math.sqrt(s)
    return int(sq) if sq == int(sq) else int(sq) +1
    
print(square_pi(3))