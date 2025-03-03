# https://www.codewars.com/kata/557b75579b03996942000061

def serve(food, flavour, mouths):
    b = 0
    for i in range(mouths):
        b += flavour ** i
    a = food / b
    lis = [round(a, 3)]
    for i in range(1, mouths):
        a = a * flavour
        lis.append(round(a, 3))
    return lis

print(serve(100, 1.5, 3))