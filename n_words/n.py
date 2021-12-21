def function(x):
    f=open('1.txt','r', encoding="utf-8")
    f=f.read()
    print(f)
    f=(f.split())
    print(f[x-1])
    return (f[x-1])
x=3
function(x)

