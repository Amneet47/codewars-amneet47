# https://www.codewars.com/kata/5c8bfa44b9d1192e1ebd3d15

def warn_the_sheep(queue):
    wolf_index = queue.index('wolf')
    if wolf_index == len(queue) - 1:
        return 'Pls go away and stop eating my sheep'
    else:
        n = len(queue) - wolf_index - 1
        return ('Oi! Sheep number ' + str(n) + '! You are about to be eaten by a wolf!')
    
print(warn_the_sheep(["sheep", "sheep", "sheep", "wolf", "sheep"]))