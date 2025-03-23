# https://www.codewars.com/kata/588810c99fb63e49e1000606

def house_of_cats(legs):
    
    possible_people_counts = []
    for num_people in range(0, legs // 2 + 1):  # Iterate through possible people counts
        remaining_legs = legs - (num_people * 2)
        if remaining_legs % 4 == 0:  # Check if remaining legs can be cats
            possible_people_counts.append(num_people)

    return possible_people_counts

print(house_of_cats(44))