# https://www.codewars.com/kata/5889ae4f7af7f99a9a000019

def draw_rectangle(canvas, rectangle):
    x1 = rectangle[0]
    y1 = rectangle[1]
    x2 = rectangle[2]
    y2 = rectangle[3]
    
    canvas[y1][x1] = '*'
    canvas[y1][x2] = '*'
    canvas[y2][x1] = '*'
    canvas[y2][x2] = '*'
    
    for i in range(x1 + 1, x2):
        canvas[y1][i] = '-'
        canvas[y2][i] = '-'
    
    for j in range(y1 + 1, y2):
        canvas[j][x1] = '|'
        canvas[j][x2] = '|'
    
    return canvas
    

canvas = [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
          ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']]
rectangle = [1, 1, 4, 3]

result = draw_rectangle(canvas, rectangle)
for row in result:
    print(row)
    
# def draw_rectangle(canvas, rectangle):
#     x0, y0, x1, y1 = rectangle
#     for x in range(x0, x1):
#         canvas[y0][x] = canvas[y1][x] = '-'
#     for y in range(y0, y1):
#         canvas[y][x0] = canvas[y][x1] = '|'
#     canvas[y0][x0] = canvas[y0][x1] = \
#         canvas[y1][x0] = canvas[y1][x1] = '*'
#     return canvas