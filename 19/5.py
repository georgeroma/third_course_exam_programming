'''
Псевдогенератор псевдослучайных чисел работает одинково, я пробовал менять через random.seed(x), но нет
если хотите получить адекватный массив 3х3, то раскоментируйте коментраии,
либо заполняйте нужный сами 

'''


import random
import __future__
#a=random.randint(0,100)#можно написать просто random.random()*100, тогда получим число с плавающей точкой
arr=[]
n=int(input('Enter n '))
arr = [[0]*n]*n #Заполняем пустыми числами
for i in range (int(n)):
    
    for j in range (int(n)):
        
        arr[i][j]=random.randrange(100)



maxx_number=arr[0][0]


#n=3
#arr=[[5],[3],[8]],[[6],[7],[2]],[[1],[4],[11]]


maxx_number=arr[0][0]
savei=0
savej=0



#maxx_number=int(maxx_number[0])





for i in range (n):
    print(*[arr[i][j] for j in range(n)])
for i in range (len(arr)):
    for j in range (len(arr)):
        
       
        x=arr[i][j]
        #x=x[0]

        
        if int(x)>int(maxx_number):
            maxx_number=arr[i][j]
            #maxx_number=int(maxx_number[0])
            savei=i
            savej=j

print(maxx_number)


for j in range (n):#Переставили первый и нужный столбец
    
    arr[0][j],arr[savei][j]=arr[savei][j],arr[0][j]

for j in range (n):#Переставили первый и нужный строка
    
    arr[j][0],arr[j][savej]=arr[j][savej],arr[j][0]

for i in range (n): #вывели
    print(*[arr[i][j] for j in range(n)])






'''# первой строкой, только для python 2
from __future__ import print_function

for i in range(5):
    print(*[a[i,j] for j in range(5)])'''