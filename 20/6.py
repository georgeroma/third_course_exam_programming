#Автор -  НАзвание альбома - год выпуска - стоимость - список песен  
audio={
'0':['Slipknot','The Studio Album Collection 1999–2008',2014,20,['Eyeless','Wait and Bleed','Surfacing','Spit It Out','Tattered & Torn','Me Inside','Liberate']],
'1':['Raizer','Resurrection',2021,35,['Resurrection','Phoenix','Invisible','Explode','Precious']]
}

ids=['0','1']

for i in ids:
    x = str(audio[i])
    x=x.replace('[','')
    x=x.replace(']','')
    x=x.replace("'",'')
    print(x)
