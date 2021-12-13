def factorial(number):
    x=1
    for i in range (1,number+1):
        
        x=x*i
        #print(x)
    if number ==0:
        #print(1)
        return 1
    return x
    


n=int(input ('Enter n '))
k=int(input ('Enter k '))
a= factorial(n)/(factorial((n-k)))
print(int(a))