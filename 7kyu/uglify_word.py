# https://www.codewars.com/kata/5ce6cf94cb83dc0020da1929

def uglify_word(s):
    flag = True  # Start with uppercase
    result = []

    for char in s:
        if char.isalpha():
            result.append(char.upper() if flag else char.lower())  
            flag = not flag
        elif char == '-':
            result.append(char)
            flag = True
        elif char == ' ':
            result.append(char)
            flag = not flag
        else:
            result.append(char)
            flag = True

    return ''.join(result) 

# print(uglify_word("aaa-bbb-ccc"))

# ("AAA"), "AaA")
# ("AaA"), "AaA")
# ("BbB"), "BbB")
# ("aaa-bbb-ccc"), "AaA-BbB-CcC")
# ("AaA-BbB-CcC"), "AaA-BbB-CcC")
# ("eeee-ffff-gggg"), "EeEe-FfFf-GgGg")
# ("EeEe-FfFf-GgGg"), "EeEe-FfFf-GgGg")
# ("qwe123asdf456zxc"), "QwE123AsDf456ZxC")
# ("Hello World"), "HeLlO WoRlD")
