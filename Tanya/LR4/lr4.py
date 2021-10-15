myString = input("Введите строку: ")
word = input("Введите искомое слово: ")

count = 0

if word in myString:
    count += 1

print("Слово", word, "встречается в строке", count, "раз")

input()