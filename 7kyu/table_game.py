# https://www.codewars.com/kata/58aa7f18821a769a7d000190

def table_game(table):
    tab = sum(table, [])
    ali = [tab[0], tab[2], tab[6], tab[8]]
    if tab[4] == tab[0] + tab[2] + tab[6] + tab[8] and tab[3] == tab[0] + tab[6] and tab[1] == tab[0] + tab[2] and tab[5] == tab[2] + tab[8] and tab[7] == tab[6] + tab[8]:
        return ali
    else:
        return -1

print(table_game([[3,7,4],[5,16,11],[2,9,7]]))

# def table_game(table):
#     (a, ab, b), (ac, abcd, bd), (c, cd, d) = table
#     if (a + b == ab) and (c + d == cd) and (a + c == ac) and (b + d == bd) and (a + b + c + d == abcd):
#         return [a, b, c, d]
#     return [-1]