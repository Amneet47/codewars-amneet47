# https://www.codewars.com/kata/5470ae03304c1250b4000e57

# def identify_weapon(character):
#     tbl = {
#       "Laval"    : "Laval-Shado Valious",
#       "Cragger"  : "Cragger-Vengdualize",
#       "Lagravis" : "Lagravis-Blazeprowlor",
#       "Crominus" : "Crominus-Grandorius",
#       "Tormak"   : "Tormak-Tygafyre",
#       "LiElla"   : "LiElla-Roarburn"
#     }
    
#     return tbl.get(character, "Not a character")

def identify_weapon(character):
    weapon_dict = {
        'Laval': 'Laval-Shado Valious',
        'Cragger': 'Cragger-Vengdualize',
        'Lagravis': 'Lagravis-Blazeprowlor',
        'Crominus': 'Crominus-Grandorius',
        'Tormak': 'Tormak-Tygafyre',
        'LiElla': 'LiElla-Roarburn'
            }
    if character not in weapon_dict:
        return "Not a character"
    else:
        return weapon_dict[character]