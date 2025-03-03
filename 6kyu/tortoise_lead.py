# https://www.codewars.com/kata/55e2adece53b4cdcb900006c

def race(v1, v2, g):
    if v2 > v1:
        tim = int((g / (v2 - v1))* 3600)
        hours = tim // 3600
        min = (tim % 3600) // 60
        sec = (tim % 3600) % 60
        return [int(hours), int(min), int(sec)]
    else: return None
    
print(race(820, 81, 550))