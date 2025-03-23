# https://www.codewars.com/kata/57acc8c3e298a7ae4e0007e3

def longest_collatz(arr):
    collatz_list = []
    def collatz(n):
        length = 1
        while True:
            if n % 2 == 0:
                n = int(n * 0.5)
                length += 1
            elif n == 1:
                break
            else:
                n = (3 * n) + 1
                length += 1
        return length
    for i in arr:
        collatz_list.append(collatz(i))
        
    return arr[collatz_list.index(max(collatz_list))]
    

print(longest_collatz([1, 5, 27, 4]))
    