k1=['70', '61', '6D', '61', '67', '69', '74', '65']
k2=[]
k3=['6B', '75', '68', '61', '63', '63', '63', '63']
salt=['73', '70', '61', '74', '70', '6C', '73', '73']
flag=[]
temp_flag=[]
for i in range(len(k1)):
    k2.append((hex(int(k1[i],16)^int(k3[i],16))[2:]))

print(k1)
print(k2)
print(k3)

for i in range(len(k1)):
    temp_flag.append((hex(int(k1[i],16)^int(k2[i],16))[2:]))

print(temp_flag)

for i in range(len(k1)):
    flag.append((hex(int(temp_flag[i],16)^int(salt[i],16))[2:]))
print(salt)
print(flag)