# https://www.codewars.com/kata/5600e00e42bcb7b9dc00014e

def harmon_point_trip(xA, xB, xC):
    xD = ((xA * xC) + (xB * xC) - (2 * (xA * xB))) / ((2 * xC) - xA - xB)
    result = round(xD, 4)
    return result

print(harmon_point_trip(2, 10, 20))