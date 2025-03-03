# https://www.codewars.com/kata/58ed139326f519019a000053

def box(coords):
    x_coor = []
    y_coor = []
    for coord in coords:
        x_coor.append(coord[0])
        y_coor.append(coord[1])
    
    r_dict = {"nw": [max(x_coor), min(y_coor)], "se": [min(x_coor), max(y_coor)]}
    return r_dict

print(box([[ -32, -143 ], [ 68, 165 ], [ -32, -130 ], [ -14, 118 ], [ -48, -136 ], [ 15, 29 ], [ -70, 50 ], [ -14, -179 ], [ 35, -72 ], [ 8, -19] ]))