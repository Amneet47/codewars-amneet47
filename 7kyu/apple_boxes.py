# https://www.codewars.com/kata/58846b46f4456a8919000025

def apple_boxes(k):
    even_sum = 0
    odd_sum = 0
    for i in range(1, k+1):
        if i % 2 == 0:
            even_sum += i * i
        else:
            odd_sum += i * i
    return (even_sum - odd_sum)

print(apple_boxes(5))