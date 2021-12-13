import __future__
n=3 # сколько на сколько матрица
arr=[[1],[3],[7]],[[8],[5],[2]],[[12],[5],[6]] #Описываем двумерный массив из вложенных списков 3х3
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


print('\n'+str(minimal_value), maximal_value)
print (max_x,max_y)
print (min_x,min_y)

print('Их разность =',((maximal_value[0])-(minimal_value[0])))#Тут достаточно странное преобразование, сразу список в инт мы не можем, а если взять знначение по его индексу, то нормально
if min_x == max_x :
    print('Общая строка:',max_x+1,'(считая с 1, а не с 0)')
elif min_y == max_y:
    print('Общий столбец:',max_y+1,'(считая с 1, а не с 0)')    
else:
    print('Ничего общего')

