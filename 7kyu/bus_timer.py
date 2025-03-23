# https://www.codewars.com/kata/5736378e3f3dfd5a820000cb

def bus_timer(current_time):
    hours, minutes = map(int, current_time.split(':'))
    minu = (hours * 60) + minutes
    if minu >= 355 and minu <= 1435:
        if ((minu + 5) // 15) == 0:
            return 0
        else:
            arrival_time = (minu % 15) + 5
            if arrival_time <= 15:
                return (15 - arrival_time)
            else: return (30 - arrival_time)
    elif minu > 1435:
        return (360 - ((minu + 5) - 1440))
    else:
        if minu + 5 >= 360:
            final = (15 - ((minu + 5) - 360))
            if final <= 5:
                return 0
            else: return (15 - final)
        else: return (360 - (minu + 5))
        
            
print(bus_timer("10:00"))
print(bus_timer("15:05"))
print(bus_timer("06:10"))
    