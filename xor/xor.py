'''Инструкция
В папку с файлом помещаете три файл: 1 - исходник и 2,3 создаёте пустые файлы с таким же расширением
Уповаю на ваше понимание ксора
В ключ вводите 16-ричное значение
и два файла укажите, они там коментариями помечены (где открываются) - с первого считывается, во второй записывается 


'''

import binascii
from os import write

#------------------------------------
f = open('output.pdf','rb')
#------------------------------------

f=f.read()
#f=(binascii.hexlify(f.encode('ANSI'))) # utf9 utf16 Windows-1251 ANSI зависит от кодировки 
print(f)
print(len(f))

print('-----------------------------------------------------')
f=bytearray(f)
x=[]
for i in range(len(f)):
    x.append( (hex(int( str(f[i]).encode( 'ANSI' )))[2:]))
#print(x)
f=[]
for i in range (len (x)):
    f.append(x[i])
print(f)
print('-----------------------------------------------------')

def solution(s):
    a_list = []
    result=s if len(s)%2==0 else f'{s}_'
    for e in range(0, len(result),2):
        a_list.append(result[e:e+2])
    return a_list

'''f=(solution(str(f)))
print(type(f))
del f[0]
del f[len(f)-1]
print(f)

print(type(f[0]))'''

#print(hex(int(f[1],16)^int('b',16))[2:])

def ascii_to_hex_converte(): #Эта функция нормально переводит строку, но херово переводит числа 
    key=['h','u','i']
    for  i in range (len (key)):
        key[i]=hex(ord(str(key[i])))[2:]
    print(key)

#-------------------
key = ['b','c','d']
#--------------------


def equality_len_key():
    global key
    global f
    copy_key=key[:]
    while len (key) < len(f):
        key+=copy_key

    while len (key) != len(f):
        del key[len(key)-1]
    print(f)
    print(key)

equality_len_key()

xor_data=[]
for i in range (len(f)):
    xor_data.append( hex( int(f[i],16) ^ int(key[i],16) ) [2:] )

for i in range (len(xor_data)):
    if len(xor_data[i])==1:
        xor_data[i]=('0'+ xor_data[i])

    '''if xor_data[i]=='1':
        xor_data[i]='01'
    if xor_data[i]=='2':
        xor_data[i]='02'
    if xor_data[i]=='3':
        xor_data[i]='03'
    if xor_data[i]=='4':
        xor_data[i]='04'
    if xor_data[i]=='5':
        xor_data[i]='05'
    if xor_data[i]=='6':
        xor_data[i]='06'
    if xor_data[i]=='7':
        xor_data[i]='07'
    if xor_data[i]=='8':
        xor_data[i]='08'
    if xor_data[i]=='9':
        xor_data[i]='09'
    if xor_data[i]=='0':
        xor_data[i]='00'''
        

print(xor_data)

#------------------------------------------------------------------------------- Создали поксоренный лист

#------------------------------------
unreadable_file=open('output2.pdf','wb')
#------------------------------------

str=''
str=str.join(xor_data)
#str = str(xor_data[i])
str_mod = binascii.unhexlify(str)
print (str_mod)
unreadable_file.write(str_mod)
