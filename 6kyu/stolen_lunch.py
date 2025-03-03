# https://www.codewars.com/kata/58884a65f06a3d3bef000049

def stolen_lunch(note):
    nums_to_letters = { 0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j' }
    letters_to_nums = {v: k for k, v in nums_to_letters.items()}
    result = ''
    for char in note:
        if char.isnumeric():
            result += nums_to_letters[int(char)]
        elif char.isalpha():
            if char in letters_to_nums:
                result += str(letters_to_nums[char])
            else:
                result += char
        else:
            result += char
    return result

print(stolen_lunch("you'll n4v4r 6u4ss 8t: cdja"))