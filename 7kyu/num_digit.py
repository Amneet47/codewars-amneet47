# https://www.codewars.com/kata/57ad85bb7cb1f3ae7c000039/

def numbers_with_digit_inside(x, d):
    num_lst = []
    for i in range(1, x+1):
        num_lst.append(str(i))
        i += 1
    filt = [num for num in num_lst if str(d) in str(num)]
    dilt = list(map(int, filt))
    if len(dilt) == 0:
        pro = 0
    else:
        pro = 1
        for j in dilt:
            pro *= j
    fin = []
    fin.append(len(dilt))
    fin.append(sum(dilt))
    fin.append(pro)
    return fin

# from functools import reduce
# from operator import mul
# def numbers_with_digit_inside(x, d):
#     numbers = [n for n in range(1, x + 1) if str(d) in str(n)]
#     return [len(numbers), sum(numbers), reduce(mul, numbers, bool(numbers))]
