myStr = input("Введите строку: ")

count = 1
max_length = 0

for i in range(len(myStr)):
   if myStr[i] == myStr[i-1] == 'н':
       count = count + 1
       if count > max_length:
           max_length = count

   else:
       count = 1

print("Самая длинная последовательность букв 'н' равна: ", max_length)
print("Строка с замененными восклицательными знаками: ", myStr.replace('!', '.'))

input()