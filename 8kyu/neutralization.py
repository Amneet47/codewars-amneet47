# https://www.codewars.com/kata/65128732b5aff40032a3d8f0

def neutralise(s1, s2):
    l = len(s1)
    res = []
    for i in range(l):
        if s1[i] == s2[i]:
            res.append(s1[i])
        else:
            res.append('0')
    return ''.join(res)