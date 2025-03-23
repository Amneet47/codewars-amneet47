# https://www.codewars.com/kata/5286b2e162056fd0cb000c20

def collatz(n):
    check_list = [n]
    while True:
        if n % 2 == 0:
            n = int(n * 0.5)
            check_list.append(n)
        elif n == 1:
            break
        else:
            n = (3 * n) + 1
            check_list.append(n)
    return "->".join(map(str, check_list))  
print(collatz(3)) 
    