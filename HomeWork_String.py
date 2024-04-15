vowels_letter = list("aeiouy")
consonants = list("bcdfghjklmnpqrstvwxz")


# Issue_1 Подсчёт гласных и согласных букв в строке
# def letter_counter(str):
#     count_vowel = 0
#     count_consonants = 0
#     for i in str:
#         if i in vowels_letter:
#            count_vowel += 1
#         else :
#             count_consonants += 1
#     return (count_consonants, count_vowel)


# user_input = input("Введите любую фразу: ")

# print(f'Количество согласных: {letter_counter(user_input)[0]}\nгласных: {letter_counter(user_input)[1]}') 


#Issue_2 Переворот строки
def string_reverser(string):
    return string[::-1]

user_input = input("Ввведите любую фразу: ")

print(f'{string_reverser(user_input)}')