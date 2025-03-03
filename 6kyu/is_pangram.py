# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram(st):
    letters = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    phrase = set(st.lower())
    if phrase >= letters:
        return True
    else: return False