# https://www.codewars.com/kata/5700c9acc1555755be00027e

def contain_all_rots(string, arr):
    rotations = [string[i:] + string[:i] for i in range(len(string))]
    for item in rotations[:]:
        for char in arr:
            if item in char:
                rotations.remove(item)
                
    if rotations == []:
        return True
    else: return False
    
print(contain_all_rots("12341234", ["DIeF", "IeFD", "12341234", "41234123", "34123412", "23412341"]))