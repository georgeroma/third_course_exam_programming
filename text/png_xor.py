import binascii
from os import write

#------------------------------------
f = open('1.txt','rb')
#------------------------------------

f=f.read()
#f=(binascii.hexlify(f.encode('ANSI'))) # utf8 utf16 Windows-1251 ANSI зависит от кодировки 
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


def ascii_to_hex_converte(): #Эта функция нормально переводит строку, но херово переводит числа 
    key=['h','u','i']
    for  i in range (len (key)):
        key[i]=hex(ord(str(key[i])))[2:]
    print(key)

#-------------------
key = ['31','32','33','34','35','36','37','38','39']
#--------------------

temp=[]
while len(key) < len(f):
    temp.append(f[0])
    del f[0]

while len(key) > len(f):
    #temp.append(f[0])
    del key[0]

print(f)
print(key)


xor_data=[]
for i in range (len(f)):
    xor_data.append( hex( int(f[i],16) ^ int(key[i],16) ) [2:] )
    

for i in range (len(xor_data)):
    if len(xor_data[i])==1:
        xor_data[i]=('0'+ xor_data[i])

print(temp)
print(xor_data)
xor_data=temp+xor_data
print (len(xor_data))

#------------------------------------------------------------------------------- Создали поксоренный лист

#------------------------------------
unreadable_file=open('2.txt','wb')
#------------------------------------

str=''
str=str.join(xor_data)
#str = str(xor_data[i])
str_mod = binascii.unhexlify(str)
print (str_mod)
unreadable_file.write(str_mod)
