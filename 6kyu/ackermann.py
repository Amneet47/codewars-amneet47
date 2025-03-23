# https://www.codewars.com/kata/53ad69892a27079b34000bd9

def Ackermann(m, n):
    
    if m == 0:
        result = (n + 1)
    elif n == 0 and m > 0:
        result = Ackermann(m-1, 1)
    else:
        result = Ackermann(m-1, Ackermann(m, n-1))
        
    return result

print(Ackermann(4, 0))