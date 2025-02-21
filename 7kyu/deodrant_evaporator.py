# https://www.codewars.com/kata/5506b230a11c0aeab3000c1f

def evaporator(content, evap_per_day, threshold):
    day = 0
    rem = 100
    while rem > threshold:
        rem -= (rem * evap_per_day) / 100
        day += 1
    return day