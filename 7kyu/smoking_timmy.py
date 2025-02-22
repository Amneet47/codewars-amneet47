# https://www.codewars.com/kata/5a0aae48ba2a14cfa600016d

def start_smoking(bars,boxes):
    cig = ((bars * 10) + boxes) * 18
    cig_final = cig
    stub = cig
    while stub >= 5:
        new = stub // 5
        cig_final += new
        rem = stub % 5
        stub = new + rem
    return cig_final