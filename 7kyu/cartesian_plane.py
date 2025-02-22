# https://www.codewars.com/kata/559e3224324a2b6e66000046

def sumin(n):
    summin = 0
    j = (2 * n) - 1
    for i in range(1, n + 1):
        summin += (i * j)
        i += 1
        j -= 2
    return summin
        
def sumax(n):
    summax = 0
    j = 1  
    for i in range(1, n + 1):
        summax += (i * j)
        j += 2
    return summax
    
def sumsum(n):
    return (sumin(n) + sumax(n))

print(sumax(5))

# Further solutions: https://www.codewars.com/kata/559e3224324a2b6e66000046/solutions/python