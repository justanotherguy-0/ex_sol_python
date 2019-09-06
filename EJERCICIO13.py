F1=[0]*3
F2=[0]*3   
print("Ingrese los datos de la primera fecha")
F1[0],F1[1],F1[2]=int(input("Dia: ")),int(input("Mes: ")),int(input("Ano: "))
print("Ingrese los datos de la segunda fecha")
F2[0],F2[1],F2[2]=int(input("Dia: ")),int(input("Mes: ")),int(input("Ano: "))
def daycount(a):
    meses=(31,28,31,30,31,30,31,31,30,31,30,31)  
    bdays=a[2]//4 +1
    if a[2] % 4==0 and (a[1]== 1 or (a[1]==2 and a[0]<=29)):
        bdays=bdays-1
    days=a[2]*365 + int(sum(meses[0:a[1]-1])) + a[0] + bdays
    return(days)
print("Diferencia de dias= ",abs(daycount(F1)-daycount(F2)))