# Дан одномерный массив, состоящий из N вещественных элементов. Ввести массив с клавиатуры. Найти и вывести минимальный по модулю элемент. Вывести массив на экран в обратном порядке.

list = []

N = int(input("Введите количество элементов списка: "))
print("Введите элементы списка: ")

for i in range(N):
    a = int(input())
    list.append(a)

abs_min = abs(list[0])

for i in range(len(list)):
    if abs(list[i]) < abs_min:
        abs_min = abs(list[i+1])

print("Минимальный по модулю элемент списка: ", abs_min)

list.reverse()
print("Список в обратном порядке", list)

input()