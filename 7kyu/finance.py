# https://www.codewars.com/kata/559ce00b70041bc7b600013d

def finance(n):
    return (n * (n + 1) * (n + 2)) // 2
print(finance(5))  # Output: 168

# def finance(n):
#     s = 0
#     p = 0
#     for i in range(n+1):
#         s += 3 * (i)
#         p += s
#     return p

# print(finance(6))
