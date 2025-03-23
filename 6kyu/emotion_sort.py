# https://www.codewars.com/kata/5a86073fb17101e453000258

def sort_emotions(arr, order):
    emotions = {
        ':D': 1, ':)': 2, ':|': 3, ':(': 4, 'T_T': 5
    }
    emotions_reverse = {value: key for key, value in emotions.items()}
    if arr is []:
        return arr
    else:
        emo_list = [emotions.get(element) for element in arr]
    
        if order:
            return_list = sorted(emo_list)
        else:
            return_list = sorted(emo_list, reverse=True)
            
        return [emotions_reverse.get(element) for element in return_list]
    
print(sort_emotions([ ':D', 'T_T', ':D', ':(' ], True))
            
# def sort_emotions(arr, order):
#     return sorted(arr, key=[':D',':)',':|',':(','T_T'].index, reverse=not order)