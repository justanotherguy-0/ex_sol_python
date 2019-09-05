def decimal(a):
    a=a-int(a)
    #Returns the binary form of the imput's decimals
    st=''
    while not(a==0):
        a*=2
        st+=str(int(a))
        a-=int(a)
    return st    
def integer(a):
    st=''
    a=int(a)
    while not(a==0):
        st+=str(a%2)
        a=int(a/2)
    return (st[::-1])    
v=float(input('Type value: '))
auxl=[]
if v-int(v)==0:
    d=integer(v)
else:
    if int(v)==0:
        d='0.'+decimal(v)
    else:     
        d=integer(v)+'.'+decimal(v)
auxl.extend(d)
print('Binary form=',d,'\nQuantity of 1s=' ,auxl.count('1'))
