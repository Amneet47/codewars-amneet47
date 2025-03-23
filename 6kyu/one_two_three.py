# https://www.codewars.com/kata/5873b2010565844b9100026d

def one_two_three(n):
    if n == 0:
        return [0, 0]
    else:
        second = int("".join(['1'] * n))
        if n <= 9:
            first = n
        else:
            rem = n % 9
            count = n // 9
            if rem == 0:
                first = int(''.join(['9'] * count))
            else:
                first = int(''.join((['9'] * count)) + str(rem))
            
        return [first, second]
    
print(one_two_three(87))