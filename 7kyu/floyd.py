# https://www.codewars.com/kata/5b096efeaf15bef812000010

def nth_floyd(n):
    value = 1
    diff = 1
    count = 0
    last_valid = 1  # Stores the last number that was < n

    while value < n:
        last_valid = value  # Update the last valid number
        value += diff
        diff += 1
        
    if value > n:
        return diff - 1
    else:
        return diff


print(nth_floyd(22))
