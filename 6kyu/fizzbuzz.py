# https://www.codewars.com/kata/5645d1a4d907bd6009000052

def fizz_buzz_factory(arr):
    fizz_dict = {item[0]: item[1] for item in arr}
    keys = [item[0] for item in arr]
    keys.sort()

    def fizz_buzz(x):
        result = ""
        for i in keys:
            if x % i == 0:
                result = fizz_dict.get(i)
        if result:
            return result
        else:
            return str(x)

    return fizz_buzz