#1 Задание
try:
    num = int(input("Введите целое число: "))

    if num % 2 == 0:
        if num == 0:
            print("нулевое число")
        elif num > 0:
            print("положительное четное число")
        else:
            print("отрицательное четное число")
    else:
        print("число не является четным")

except ValueError:
    print("Ошибка: Введите корректное целое число.")

#2 Задание
word = input("Введите слово из маленьких латинских букв: ")

if not word.islower() or not word.isalpha():
    print("Ошибка: Введите слово, состоящее только из маленьких латинских букв.")
    exit()

vowels = ['a', 'e', 'i', 'o', 'u']

count_consonants = 0
count_vowels = 0
vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in word:
    if char in vowels:
        count_vowels += 1
        vowel_counts[char] += 1
    else:
        count_consonants += 1

print(f"Согласных: {count_consonants}")
print(f"Гласных: {count_vowels}")

for vowel in vowels:
    if vowel_counts[vowel] > 0:
        print(f"{vowel}: {vowel_counts[vowel]}")
    else:
        print(f"{vowel}: False")

#3 задание
try:
    X = float(input("Введите минимальную сумму инвестиций (X): "))
    A = float(input("Введите сумму у Майкла (A): "))
    B = float(input("Введите сумму у Ивана (B): "))

    if X <= 0 or A < 0 or B < 0:
        print("Ошибка: суммы должны быть положительными (X > 0, A >= 0, B >= 0).")
        exit()

    mike_can = A >= X
    ivan_can = B >= X
    together_can = (A + B) >= X

    if mike_can and ivan_can:
        print(2)
    elif mike_can:
        print("Mike")
    elif ivan_can:
        print("Ivan")
    elif together_can:
        print(1)
    else:
        print(0)

except ValueError:
    print("Ошибка: введите корректные числа.")