print('Пирамидка 2')

# Программа получает на вход количество уровней пирамиды и выводит их на экран.

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

height = int(input('Введите высоту: '))
first_number = 1

for i in range(height + 1):
    string = '\t' * (height - i)
    for j in range(i):
      string += str(first_number) + '\t\t'
      first_number += 2
    print(string)
