from os import close
'''Как это всё работает
Для начала есть два типа разделений  чисел в исходном файле: через пробелы и через энтер (\n) - Я привожу всё к \n
После этого есть функция которая находит минус и пока не встретит '\n' записывает эти числа в файл, но сначала надо разобраться с нулями:
если ноль первое и последующие числа, то я идаляю его из списка и записываю в файл h чтобы он потом не путался под ногами, там конечно придётся удалить двойные энтеры но это уже там да
потом просто записываются положительные числа
потом открываются файлы g и h и из них удаляются лишние энтеры

'''
#-------------------------------------------------------------------------
#ВНИМАНИЕ НЕ ОСТАВЛЯЙТЕ ЛИШНИЙ ЭНТЕР В КОНЦЕ ФАЙЛА ИНПУТ ИЛИ ЛИШНИЙ ПРОБЕЛ
#-------------------------------------------------------------------------

f=open('input.txt','r')
#f=open('input2.txt','r')
f=f.read()
f = list(f)

for i in range (len(f)):
    if f[i]==' ':
        f[i]='\n'
debug=0       



g=open('g.txt','w')
h=open('h.txt','w')

print(f)
for i in range (len(f)):
    if f[0]=='0':
        f.remove(f[0])
        h.write('0')
        h.write('\n')

for i in range (len(f)):
    try:
        if f[i]=='0' and f[i-1]=='\n' and f[i+1]=='\n' :
            f.remove(f[i])
            
            h.write('0')
            h.write('\n')
            i-=1 
    except:
        pass
print (f)
def write_minus_variable():
    plus=[]
    print (len(f))
    #for i in range(len(f)): #Оно без трая не работает правильно, я хз
        #try:
        
            #f.remove(' ')
        #except:
            #pass

    print (f)
    
    for i in range (len(f)):
        #print(f[i])
        if f[i]=='-':
            try:
                while f[i]!='\n':
                    plus.append(f[i])
                    i+=1
            except:
                i-=1
                
            
            if f[i]=='\n':
                plus.append('\n')
                
                h.write(''.join(plus))
                plus=[]
            
            try:
                f[i]+1
            except:
                plus.append('\n')
                
                h.write(''.join(plus))
                plus=[]



print(f)       
def   write_plus_wariable():
    plus=[]
    try:
        for i in range (len(f)):
            
            
            if f[i]!='-' and f[i]!='\n':
                
                plus.append(f[i])
            
            if f[i]=='\n':
                plus.append('\n')
                g.write(''.join(plus)) 
                plus=[]

            if f[i]=='-':
                try:
                    while f[i]!='\n':
                        #print(f[i])
                        f.remove(f[i])
                    
                        
                except:
                    break 
    except:
        if plus[0]=="0":
            global debug
            debug=1 #Это какой-то баг с нулём и я не знаю как что и почему, у меня итак 200 строк спасите!!!!!!!!!!!!!!
        else:
            print(plus)
            plus.append('\n')
            g.write(''.join(plus)) 
            plus=[]


#---------------------------------    
write_minus_variable()          
write_plus_wariable()           
g.close()                       
h.close()                       
#--------------------------------- 


def remove_enters_g():
    g=open('g.txt','r')
    
    g=g.read()
    g = list(g)
    
    #print(g)
    #print(h)

    for i in range(len(g)):
        try:
            if g[0]=='\n':
                g.remove(g[0])
        except:
            pass
    #print(g)
    for_delet=[]
    for i in range(len(g)):
        try:
            if g[i]=='\n' and g[i+1]=='\n':
                #print(g[i].index())
                for_delet.append(i)
                #print(i,i+1)
                #g.remove(g[i])
                
        except:
            pass
    for i in range(len(for_delet)):
        g[for_delet[i]]='$'
    for i in range(len(for_delet)):    
        g.remove('$')
    
        
    #print(g)
    copy_g=g
    
    g=open('g.txt','w')
    for i in range(len(copy_g)):
        g.write(copy_g[i])



def remove_enters_h():
    h=open('h.txt','r')
    
    h=h.read()
    h = list(h)
    
    #print(h)
    #print(h)

    for i in range(len(h)):
        try:
            if h[0]=='\n':
                h.remove(h[0])
        except:
            pass
    #print(h)
    for_delet=[]
    for i in range(len(h)):
        try:
            if h[i]=='\n' and h[i+1]=='\n':
                #print(g[i].index())
                for_delet.append(i)
                #print(i,i+1)
                #g.remove(g[i])
                
        except:
            pass
    for i in range(len(for_delet)):
        h[for_delet[i]]='$'
    for i in range(len(for_delet)):    
        h.remove('$')
    
        
    #print(h)
    copy_h=h
    
    h=open('h.txt','w')
    for i in range(len(copy_h)):
        h.write(copy_h[i])
    
    global debug
    
    if debug==1:#Не обращайте внимания
    
        #h.seek(1)
        #h.write('\n')
        h.write('0')
        

    

remove_enters_g()
remove_enters_h()

















# Это я игрался с рандомным заполнением 
"""import random
def writeforfile():
    input = open("input2.txt",'w')
    for i in range (100):
        #print (round((random.random()*10),2))
        input.write(str((round(int((random.random()*10)))))+" ")
    input.close()
writeforfile()
f=open('input2.txt','r')

text = f.readlines()
text=str(text)
text=text.replace(" ", "\n")
text=text.replace("['", "")
text=text.replace("']", "")
f.close
f=open('input2.txt','w')
f.write(str(text))
print(f)
print (text)
f.close

f=open('input2.txt','r')
text = f.readlines()
print(text)
min = text[1]

for i in range (len(text)):
    if text[i]<min:
        min = text[i]
print(min)
#"""