# https://www.codewars.com/kata/5ce9c1000bab0b001134f5af

def quarter_of(month):
    # your code here
    match month:
        case 1 | 2 | 3:
            return 1
        case 4  | 5 | 6:
            return 2
        case 7 | 8 | 9:
            return 3
        case 10 | 11 | 12:
            return 4