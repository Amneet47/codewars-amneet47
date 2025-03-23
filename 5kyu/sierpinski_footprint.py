# https://www.codewars.com/kata/5be0af91621daf08e1000185

def find_closest_value(m):
    n = 1
    sum_values = 0
    valid_n_values = []
    
    if m == 1:
        return 4
    
    else:
        while True:
            if (4 * n**2 + 1) % 65 == 0:
                valid_n_values.append(n)

            next_n = n+1

            if (4 * next_n**2 + 1) % 65 == 0:
                pass
            else:
                if len(valid_n_values)> 0:
                    current_sum = sum(valid_n_values)
                    if current_sum > m:
                        sum_values2 = current_sum
                        break
                    sum_values = current_sum
                n+=1
                continue
            n += 1
    if m - sum_values < sum_values2 - m:
        return sum_values
    else:
        return sum_values2

print(find_closest_value(5000))