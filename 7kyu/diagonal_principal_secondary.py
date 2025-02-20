# https://www.codewars.com/kata/5a8c1b06fd5777d4c00000dd

def diagonal(matrix):
    l = len(matrix)
    prim = []
    seco = []
    for i in range(len(matrix)):
        prim.append(matrix[i][i])
        seco.append(matrix[i][l-1-i])
    p_sum = sum(prim)
    s_sum = sum(seco)
    if p_sum == s_sum:
         return "Draw!"
    elif p_sum < s_sum:
         return "Secondary Diagonal win!"
    else:
         return "Principal Diagonal win!"
    pass