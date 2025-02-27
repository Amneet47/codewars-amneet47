def leonardo_numbers(n, L0, L1, add) :
    l = [L0, L1]
    i = 2
    while i < n:
        nex = l[i-1] + l[i-2] + add
        l.append(nex)
        i += 1
    return l

print(leonardo_numbers(5, 1, 1, 1))