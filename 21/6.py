from datetime import datetime
parom = {
 '0':  [ 'Симферополь','12:30','13:45','',228],
 '1':  [ 'Севастополь','14:30','16:50','',1337],
 '2':  [ 'Ялта','18:30','18:35','',7]}
ids=['0','1','2']
for i in ids:
    time_1=parom[i][1]
    time_2=parom[i][2]
    time_1=datetime.strptime(time_1,"%H:%M") #У нас питонистов есть библиотеки для подсчёта времени 
    time_2=datetime.strptime(time_2,"%H:%M")
    #print(time_1.hour,':',time_1.minute)
    #print(time_2.hour,':',time_2.minute)
    time_interval=time_2-time_1

    parom[i][3]=str(time_interval)

    print(parom[i])