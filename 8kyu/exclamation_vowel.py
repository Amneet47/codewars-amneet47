# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

def replace_exclamation(st):
    vow = "aeiouAEIOU"
    return ''.join('!' if char in vow else char for char in st)