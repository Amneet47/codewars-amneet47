# https://www.codewars.com/kata/586a1af1c66d18ad81000134

def driver(data):
    # Start driving here!
    data_0 = data[0]
    data_1 = data[1]
    data_2 = data[2]
    data_3 = data[3]
    data_4 = data[4]
    licence = []
    
    if len(data_2) >= 5:
        licence.append((data_2[0:5]).upper())
    else:
        licence.append(data_2.upper().ljust(5, '9'))
        
    year = data_3.split("-")[-1]
    month = (data_3.split("-")[-2])[:3]
    licence.append(year[2])
    
    mon = {
        'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12
    }
    
    if data_4 == 'M':
        licence.append(f"{mon.get(month, 0):02d}")
    elif data_4 == 'F':
        licence.append(str(mon.get(month) + 50))
        
    licence.append(data_3.split("-")[-3])
    licence.append(year[-1])
    licence.append(data_0[0])
    if data_1 == "":
        licence.append('9')
    else: licence.append(data_1[0])
    
    licence.append('9AA')
        
    return ''.join(licence)

print(driver(["John", "James", "Smith", "01-Jan-2000", "M"]))

LEE99800021AR9AA
LEE99809021AR9AA