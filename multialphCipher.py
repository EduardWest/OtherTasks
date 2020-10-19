from itertools import cycle

def rotated_letter(letter, key):
    if letter.isalpha():    
        num = ord(letter) - ord("a") + key

        if num == 0: 
            return "z"

        return chr(num % 26 + ord("a"))

    else:
        return letter


def rotated_word(word, shifts):
    new_word = ""

    shifts_cycle = cycle(shifts)
    for letter in word:
        shift = next(shifts_cycle)
        new_letter = rotated_letter(letter, shift)
        new_word += new_letter

    return new_word 

def get_key():
    while True:   
        try:
            key = input('Input the key:\n').lower()

            if key.isalpha():
                shifts = []
                for letter in key:
                    shifts.append(ord(letter) - ord("a") + 1)
                return shifts

        except:
            print("\nPlease enter a valid key.\n")


def get_mode():
    while True:
        mode = input('Enter E to encode or D to decode:\n').upper()

        if mode in ('E', 'D'):
            return mode


def main():
    word =  input('Input the text:\n').lower()

    shifts = get_key()

    mode = get_mode()

    if mode == 'E':
        print(rotated_word(word, shifts))
    else:
        negative_shifts = list(-x for x in shifts)
        print(rotated_word(word, negative_shifts))
