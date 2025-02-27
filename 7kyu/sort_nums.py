# https://www.codewars.com/kata/5174a4c0f2769dd8b1000003

def solution(nums):
    if nums is None:
        return []
    elif nums == []:
        return []
    else:
        return sorted(nums)
    
    
print(solution([1,2,3,10,5]))