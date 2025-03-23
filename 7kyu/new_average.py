def new_avg(arr, newavg):
	# your code
    donation = (newavg * (len(arr) + 1)) - sum(arr)
    if donation < 0:
        raise ValueError
    else: 
        if isinstance(donation, float) and donation.is_integer():
            return int(donation)
        elif isinstance(donation, int):
            return donation
        else:
            return int(float(donation)) + 1

print(new_avg([14, 30, 5, 7, 9, 11, 15], 92))