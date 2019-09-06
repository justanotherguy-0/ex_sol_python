def nlen(a):
    c=a
    lst=[]
    lst.append(a)
    while lst[len(lst)-1]!=1:
        if lst[len(lst)-1]%2==0:
            lst.append(lst[len(lst)-1]//2)
        else:
            lst.append(lst[len(lst)-1]*3 +1)
    return(len(lst))
def lstgenerator(b):
    lgt=[0]*b
    for i in range(0,b):
        lgt[i]=nlen(i+1)
    return(lgt)  

def results(l):
    m=max(l)
    gen=[]
    for k in range(0,len(l)):
        if l[k]==m:
            gen.append(k+1)
    return(gen)
n=int(input("Ingrese el limite derecho del intervalo: "))

print(results(lstgenerator(n)))
