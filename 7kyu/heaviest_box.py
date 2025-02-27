# https://www.codewars.com/kata/57b127051fae8a1d1b000104
# a < b < c < d < e
# L[n-1] and L[n-2] will be fixated for (c+e) and (d+e)

def heaviest_box(weigh):
    boxes = sorted(weigh)
    total = sum(boxes) * 0.25
    c = total - boxes[0] - boxes[9]
    e = boxes[8] - c
    return int(e)

print(heaviest_box([156,147,119,135,180,152,123,168,140,164]))