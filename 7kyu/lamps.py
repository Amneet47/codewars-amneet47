# https://www.codewars.com/kata/58a3c1f12f949e21b300005c

def lamps(a):
    check_10 = []
    check_01 = []
    if len(a) >= 2:
        if len(a) % 2 == 0:
            check_10 = [1, 0] * (len(a) // 2)
            check_01 = [0, 1] * (len(a) // 2)
        else:
            check_10 = ([1, 0] * (len(a) // 2)) + [1]
            check_01 = ([0, 1] * (len(a) // 2)) + [0]
        
        count_10 = 0
        count_01 = 0
        
        for i in range(len(a)):
            if a[i] != check_10[i]:
                count_10 += 1
            elif a[i] != check_01[i]:
                count_01 += 1
            
        return (count_10 if count_10 <= count_01 else count_01)
    else: return 0
    
print(lamps([0, 1, 0, 1, 0]))

# def lamps(a):
#     n = sum(1 for i, x in enumerate(a) if x != i % 2)
#     return min(n, len(a) - n)