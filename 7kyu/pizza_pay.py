# https://www.codewars.com/kata/5b043e3886d0752685000009

def michael_pays(cost):
    third = (cost / 3)
    if cost < 5:
        return round(cost, 2)
    else:
        if third > 10:
            return round((cost-10), 2)
        else:
            return round((cost - third), 2)