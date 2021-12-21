import time
start_time = time.time()



f=open('3.txt','rb')
f=f.read()

print(f)
words=[]


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

decima_arr=[]
for i in range(len(f)):
    decima_arr.append(int(f[i],16))

print ((decima_arr))

for i in range (len (decima_arr)):
    if decima_arr[i] >= 65 and decima_arr[i] <= 90:
        words.append(decima_arr[i])

for i in range (len(words)):
    words[i]=(chr(words[i]))


print (''.join(words))

print("--- %s seconds ---" % (time.time() - start_time))
