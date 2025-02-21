# https://www.codewars.com/kata/58ce8725c835848ad6000007

def potatoes(p0, w0, p1):
    dry = (w0 * (100 - p0)) / 100
    final = (dry * 100) / (100 - p1)
    fin = int(final)
    return fin