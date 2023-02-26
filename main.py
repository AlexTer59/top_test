import alphabets


# Проверка правильности введенного режима работы алгоритма
def is_valid_answer(answer):
    if answer == 'шифрование' or answer == 'дешифрование':
        if answer == 'шифрование':
            return True
        else:
            return False
    else:
        print("Пожалуйста, введите корректный режим работы алгоритма: шифрование/дешифрование")
        answer = input().lower()
        answer = is_valid_answer(answer)
        return answer


# Проверка правильности введенного алфавита
def is_valid_alphabet(alph_answer):
    if alph_answer == 'русский' or alph_answer == 'английский':
        if alph_answer == 'русский':
            return True
        else:
            return False
    else:
        print("Пожалуйста, введите корректный алфавит: русский/английский")
        alph_answer = input().lower()
        alph_answer = is_valid_alphabet(alph_answer)
        return alph_answer


# Проверка правильности введенного числа сдвига
def is_valid_shift(num):
    try:
        num = int(num)
        return num
    except ValueError:
        print("Введите корректную величину сдвига")
        num = input()
        num = is_valid_shift(num)
        return num


# Алгоритм шифрования
def encrypt(alph, num, txt):
    final_text = ""
    for i in range(len(txt)):
        if txt[i].isupper() and txt[i].isalpha():
            if alph:
                final_text += alphabets.ru_upper_alphabet[(alphabets.ru_upper_alphabet.find(txt[i]) + num) % 32]
            else:
                final_text += alphabets.eng_upper_alphabet[(alphabets.eng_upper_alphabet.find(txt[i]) + num) % 26]
        elif txt[i].islower() and txt[i].isalpha():
            if alph:
                final_text += alphabets.ru_lower_alphabet[(alphabets.ru_lower_alphabet.find(txt[i]) + num) % 32]
            else:
                final_text += alphabets.eng_lower_alphabet[(alphabets.eng_lower_alphabet.find(txt[i]) + num) % 26]
        else:
            final_text += txt[i]
    return final_text


# Алгоритм дешифрования
def decrypt(alph, num, txt):
    final_text = ""
    for i in range(len(txt)):
        if txt[i].isupper() and txt[i].isalpha():
            if alph:
                final_text += alphabets.ru_upper_alphabet[(alphabets.ru_upper_alphabet.find(txt[i]) - num) % 32]
            else:
                final_text += alphabets.eng_upper_alphabet[(alphabets.eng_upper_alphabet.find(txt[i]) - num) % 26]
        elif txt[i].islower() and txt[i].isalpha():
            if alph:
                final_text += alphabets.ru_lower_alphabet[(alphabets.ru_lower_alphabet.find(txt[i]) - num) % 32]
            else:
                final_text += alphabets.eng_lower_alphabet[(alphabets.eng_lower_alphabet.find(txt[i]) - num) % 26]
        else:
            final_text += txt[i]
    return final_text


# Главная программа

print("Выберите направлене работы алгоритма: шифрование/дешифрование?")
what_to_do = input().lower()
what_to_do = is_valid_answer(what_to_do)
print("Введите текст с которым необходимо работать:")
text = input()
print("Выберите алфавит: русский/английский")
what_alphabet = input().lower()
what_alphabet = is_valid_alphabet(what_alphabet)
print("Введите величину сдвига:")
shift = input()
shift = is_valid_shift(shift)
if what_to_do:
    print(encrypt(what_alphabet, shift, text))
else:
    print(decrypt(what_alphabet, shift, text))
