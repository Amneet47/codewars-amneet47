# https://www.codewars.com/kata/679e0a54f8d448b508865c3b

def estimator(obstacles, stamina):
    counts = {"1": 0, "1, 1": 0, "1, 1, 1": 0}
    current_sequence = []

    for num in obstacles:
        if num == 1:
            current_sequence.append(num)
        else:
            if current_sequence:  # Check if a sequence exists
                sequence_str = ", ".join(map(str, current_sequence))
                if sequence_str in counts:
                    counts[sequence_str] += 1
                current_sequence = []  # Reset the sequence

    # Check for a sequence at the end of the list
    if current_sequence:
        sequence_str = ", ".join(map(str, current_sequence))
        if sequence_str in counts:
            counts[sequence_str] += 1

    return_list = [counts["1"]*2, counts["1, 1"]*5, counts["1, 1, 1"]*10]
    if sum(return_list) > stamina:
        return False
    else: return True

print(estimator([0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0], 20))