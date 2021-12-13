import __future__
n=3 # сколько на сколько матрица
arr=[[1],[3],[8]],[[6],[7],[2]],[[4],[5],[11]] #Описываем двумерный массив из вложенных списков 3х3
for i in range (n): #Выводим массив
    print(*[arr[i][j] for j in range(n)])

minimal_value=arr[0][0]
maximal_value= arr[0][0]
max_x=0
max_y=0
min_x=0
min_y=0
for i in range (3): #Находим минимальный и максимальный элементы, и сохраняем их координаты (там тройка так как матрица 3 на 3 если что-то сам делать будешь то через ввод пользователя, я называл её n)
    for j in range (3):

        if arr[i][j]<minimal_value:
            minimal_value=arr[i][j]
            max_x=i
            max_y=j

        if arr [i][j]>maximal_value:
            maximal_value=arr [i][j]
            min_x=i
            min_y=j

print(minimal_value, maximal_value)
print (max_x,max_y)
print (min_x,min_y)

for i in range (3): #Смена столбцов местами (элементов в столбцах)
    arr[i][min_y],arr[i][max_y]=arr[i][max_y],arr[i][min_y]


for i in range (n): #Выводим массив
    print(*[arr[i][j] for j in range(n)])

for j in range (3):#Смена строк местами (элементов в строках)
    arr[min_x][j],arr[max_x][j]=arr[max_x][j],arr[min_x][j]

print() #Отбтвка для лучшего восприятия 

for i in range (n):#Выводим массив
    print(*[arr[i][j] for j in range(n)])