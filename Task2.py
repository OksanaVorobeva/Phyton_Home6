#Задача 32: Определить индексы элементов массива (списка), значения 
#которых принадлежат заданному диапазону 
#(т.е. не меньше заданного минимума и не больше заданного максимума)

list1=[1,5,3,7,8,2,9]
min_number=int(input("Введите min число "))
max_number=int(input("Введите max число "))
for i in range(len(list1)):
    if min_number<=list1[i] and list1[i]<=max_number:
        print(i)