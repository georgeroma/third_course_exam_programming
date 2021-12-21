import time
start_time = time.time()



f=open('3.txt','r')
f=f.read()

print(f)
words=[]
for i in range (len(f)):
    if f[i] == 'A':
        words.append(f[i])
    if f[i] == 'B':
        words.append(f[i])
    if f[i] == 'C':
        words.append(f[i])
    if f[i] == 'D':
        words.append(f[i])
    if f[i] == 'E':
        words.append(f[i])
    if f[i] == 'F':
        words.append(f[i])
    if f[i] == 'G':
        words.append(f[i])
    if f[i] == 'H':
        words.append(f[i])
    if f[i] == 'I':
        words.append(f[i])
    if f[i] == 'J':
        words.append(f[i])
    if f[i] == 'K':
        words.append(f[i])
    if f[i] == 'L':
        words.append(f[i])
    if f[i] == 'M':
        words.append(f[i])
    if f[i] == 'N':
        words.append(f[i])
    if f[i] == 'O':
        words.append(f[i])
    if f[i] == 'P':
        words.append(f[i])
    if f[i] == 'Q':
        words.append(f[i])
    if f[i] == 'R':
        words.append(f[i])
    if f[i] == 'S':
        words.append(f[i])
    if f[i] == 'T':
        words.append(f[i])
    if f[i] == 'U':
        words.append(f[i])
    if f[i] == 'V':
        words.append(f[i])
    if f[i] == 'W':
        words.append(f[i])
    if f[i] == 'X':
        words.append(f[i])
    if f[i] == 'Y':
        words.append(f[i])
    if f[i] == 'Z':
        words.append(f[i])
    
print(''.join(words))
    
print("--- %s seconds ---" % (time.time() - start_time))
