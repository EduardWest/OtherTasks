def cesar(letter,key): #кодирование одного символа
        if letter.isalpha():
            num = ord(letter) - ord("a") + key #key - количество сдвигов

            if num ==0:
                if key < 0:
                    return "a"
                else:
                    return "z"

            return chr(num % 26 + ord("a"))
        else:
            return letter

def slovo(word,key): #Кодирование целого слова и текста
        new_slovo = ""
        for letter in word:
                new_letter = cesar(letter,key)
                new_slovo+=new_letter

        return new_slovo

    
def get_key():
        while True:
                try:
                        key=int(input('Введите ключ от 1 до 25:\n')) #Просим у пользователя ввести ключ кодирования
                        if key in range(1,26):
                                return key
                except:
                    print("\nПожалуйста, повторите ввод.\n")
def get_mode():
        while True:
                mode = input("Введите E для кодировки или D для декодировки:\n").upper()

                if mode in ('E','D'):
                    return mode
def man():
        word = input('Введите текст:\n').lower()

        key = get_key()

        mode = get_mode()

        if mode == 'E':
                print(slovo(word,key))
        else:
                print(slovo(word,-key))

            
    
