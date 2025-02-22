# https://www.codewars.com/kata/55e6f5e58f7817808e00002e

def seven(m):
    step = 0
    num = m
    while num > 98:
        rem = num % 10
        nex = num // 10
        div = nex - (2 * rem)
        num = div
        step += 1
    return (num, step)