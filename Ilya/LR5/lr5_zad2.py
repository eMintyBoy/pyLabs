list = [0,1,2,3,4,5,6,7,8,9]

newList = []

for i in range(len(list)):
   if (list[i]%2==0):
      newList.append(list[i])

print("Полученный массив в порядке возрастания элементов:", newList)

input()