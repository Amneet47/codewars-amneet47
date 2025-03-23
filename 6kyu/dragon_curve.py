# https://www.codewars.com/kata/53ad7224454985e4e8000eaa

def dragon(n):
    def remove_chars(input_string, chars_to_remove):
        result = ""
        for char in input_string:
            if char not in chars_to_remove:
                result += char
        return result
    rep = {'a': 'aRbFR', 'b': 'LFaLb'}
    d0 = 'Fa'
    if isinstance(n, int) and n > 0 and not isinstance(n, bool):
        for _ in range(n):
            temp = ""
            for char in d0:
                if char in rep:
                    temp += rep[char]
                else:
                    temp += char
            d0 = temp

        chars = "ab"
        return remove_chars(d0, chars)
    elif n == 0:
        return 'F'
    else: return ''


# def Dragon(n):
#     if type(n) != int or n < 0:
#         return ""
#     stg, a, b = "F{a}", "{a}R{b}FR", "LF{a}L{b}"
#     for _ in range(n):
#         stg = stg.format(a=a, b=b)
#     return stg.replace("{a}", "").replace("{b}", "")
print(dragon(10))