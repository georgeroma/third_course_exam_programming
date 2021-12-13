klass={
'0':['Gosha',[5,5,5,5]],
'1':['Vanya',[4,4,4,4]],
'2':['Sasha',[3,3,3,3]],
'3':['Nikita',[4,5,3,4]],
'4':['lesha',[8,4,4,2]],
'5':['Anna',[3,2,3,5]],
'6':['Grisha',[5,5,3,3.5]],
}

ids=['0','1','2','3','4','5','6']

for i in ids:
    midle=0
    for j in range (4):
        midle+=klass[ids[int(i)]][1][j]
    midle /=4
    klass[ids[int(i)]]+=' '
    print(klass[ids[int(i)]][2])
    klass[ids[int(i)]][2]=str(midle)
    print (klass[ids[int(i)]])


#print(klass.items())
