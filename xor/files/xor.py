import binascii
f = open('file_for_igor.pdf','r')
f=f.read()

f=(binascii.hexlify(f.encode('utf8')))
print(f)
f=(int(f))
a=[]
a.append(f)
print(a)


'''c=list(f)
print(c)
d='11'.encode('utf-8')
print(d)
f=f^d
print (f)'''

def solution(s):
    a_list = []
    result=s if len(s)%2==0 else f'{s}_'
    for e in range(0, len(result),2):
        a_list.append(result[e:e+2])
    return a_list

f=(solution(str(f)))
xor_bytes=[]
for i in range (len(f)):
    #print(f[i])
    number=11^(int(f[i], 16))
    xor_bytes.append(number)
    #print()

print(xor_bytes)

