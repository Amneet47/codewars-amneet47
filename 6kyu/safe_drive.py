def drive(drinks, finished, drive_time):
    # Code here
    total_units = 0
    for i in drinks:
        total_units += (i[0] * i[1]) / 1000
    fin_hours, fin_minutes = map(int, finished.split(':'))
    dri_hours, dri_minutes = map(int, drive_time.split(':'))
    fin_at = fin_hours + (fin_minutes / 60)
    dri_at = dri_hours + (dri_minutes / 60)
    if dri_at >= fin_at:
        if dri_at - fin_at > total_units:
            check = True
        else: check = False
    else:
        if dri_at + (24 - fin_at) > total_units:
            check = True
        else: check = False
    return [round(total_units,2), check]


alcohol = [[5.2,568],[12.0,175]]
print(drive(alcohol, "16:00", "23:00"))

# def drive(drinks, finished, drive_time):
#     fin, driv = list(map(lambda str_t: [int(t) for t in str_t.split(':')], [finished, drive_time]))
#     delta = driv[0] - fin[0] + (driv[1] - fin[1])/60 + 24 * (driv<=fin)
#     drive_units = sum(strength * volume for strength, volume in drinks) / 1000
#     return [round(drive_units, 2), delta>drive_units]