# https://www.codewars.com/kata/589b1c15081bcbfe6700017a

def cost(mins):
    if mins <= 65:
        cost = 30
    else:
        extra = mins - 60
        if extra % 30 <=5:
            half = extra // 30
            cost = 30 + (10 * half)
        else:
            half = (extra // 30) + 1
            cost = 30 + (10 * (half))
        
    return cost