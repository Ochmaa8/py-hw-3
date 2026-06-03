word = input("Введите слово из маленьких латинских букв: ")

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
consonant_count = 0

# Словари для подсчёта каждой гласной
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0

# по каждой букве
for letter in word:
    if letter in vowels:
        vowel_count += 1
        # каждую гласную отдельно
        if letter == 'a':
            count_a += 1
        elif letter == 'e':
            count_e += 1
        elif letter == 'i':
            count_i += 1
        elif letter == 'o':
            count_o += 1
        elif letter == 'u':
            count_u += 1
    else:
        consonant_count += 1

# Выводим общее количество
print(f"Гласных: {vowel_count}")
print(f"Согласных: {consonant_count}")

# Выводим количество каждой гласной или False, если её нет
if count_a > 0:
    print(f"a: {count_a}")
else:
    print("a: False")

if count_e > 0:
    print(f"e: {count_e}")
else:
    print("e: False")

if count_i > 0:
    print(f"i: {count_i}")
else:
    print("i: False")

if count_o > 0:
    print(f"o: {count_o}")
else:
    print("o: False")

if count_u > 0:
    print(f"u: {count_u}")
else:
    print("u: False")
