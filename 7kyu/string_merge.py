# https://www.codewars.com/kata/597bb84522bc93b71e00007e/

def string_merge(string1, string2, letter):
    id1 = string1.index(letter)
    id2 = string2.index(letter)
    result = string1[:id1 +1] + string2[id2 + 1:]
    return result