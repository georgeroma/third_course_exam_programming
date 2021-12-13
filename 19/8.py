import random
def writeforfile():
    input = open("input2.txt",'w')
    for i in range (100):
        #print (round((random.random()*10),2))
        input.write(str((round((random.random()*10),2)))+" ")
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
#