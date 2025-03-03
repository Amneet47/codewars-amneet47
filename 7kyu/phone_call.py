# https://www.codewars.com/kata/588425ee4e8efb583d000088

def phone_call(min1, min2_10, min11, s):
    cost_10 = min1 + (9 * min2_10)
    rem_bal = s - cost_10
    up_11 = 10
    rem_under_10 = 0
    if rem_bal > 0:
        while rem_bal >= min11:
            up_11 += 1
            rem_bal -= min11
        return up_11
    else:
        rem_under_10 = s - min1
        return ((rem_under_10 // min2_10) + 1)
    
print(phone_call(3,1,2,20))
print(phone_call(2,2,1,2))
print(phone_call(10,1,2,22))
print(phone_call(2,2,1,24))
print(phone_call(1,2,1,6))

# def phone_call(min1, min2_10, min11, s):
#     minutes, cost = 0, min1
#     while s >= cost:
#         minutes += 1
#         s -= cost
#         if minutes == 1: cost = min2_10
#         if minutes == 10: cost = min11
#     return minutes
    