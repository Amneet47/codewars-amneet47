# https://www.codewars.com/kata/5a0599908ba914a6cf000138

def get_note(pitch):
    notes_dictionary = {
    440: "A",
    466.16: "A#",
    493.88: "B",
    523.25: "C",
    554.37: "C#", 
    587.33: "D", 
    622.25: "D#", 
    659.25: "E", 
    698.46: "F", 
    739.99: "F#", 
    783.99: "G", 
    830.61: "G#"
    }
    if pitch > 440:
        for key in notes_dictionary:
            if pitch % key == 0:
                return notes_dictionary[key]
    else:
        i = 1
        p1 = pitch
        while p1 < 830.61:
            p1 = pitch * i
            for key in notes_dictionary:
                if p1 % key == 0:
                    return notes_dictionary[key]
            i += 1