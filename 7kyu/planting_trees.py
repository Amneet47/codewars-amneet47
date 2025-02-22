def sc(width,length,gaps):
    position = (2 * width) + (2 * length) - 4
    trees = ['a'] * position
    count = 0
    lent = len(trees)
    for i in range(0, lent, gaps + 1):
        trees[i] = 'b'
        count += 1
    last_tree = trees[::-1].index('b')
    if last_tree == gaps:
        return count
    else:
        return 0

print(sc(7,7,3))