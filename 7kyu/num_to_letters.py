# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c

def switcher(arr):
    #your code here
    dict_map = {str(i): chr(123 - i) for i in range(1, 27)}
    dict_map.update({'27': '!', '28': '?', '29': ' '})
    return ''.join(dict_map[num] for num in arr)