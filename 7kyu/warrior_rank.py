# https://www.codewars.com/kata/674ee1a71e3ef76fca606009

def find_warrior_rank(skill):
    maha = skill // 10
    ati = (skill % 10)
    piti = 0
    if ati >= 3 and ati <= 7:
        piti = 1
    elif ati >= 8:
        maha += 1
        
    maha_warrior = maha * "maha-"
    ati_warrior = piti * "ati-"
    
    if ati_warrior is None and maha_warrior is None:
        warrior = "rathi"
    elif ati_warrior is None:
        warrior = maha_warrior + "rathi"
    elif maha_warrior is None:
        warrior = ati_warrior + "rathi"
    else:
        warrior = ati_warrior + maha_warrior + "rathi"
    return warrior
    
        

print(find_warrior_rank(76))
        