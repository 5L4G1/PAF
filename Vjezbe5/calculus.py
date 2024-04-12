import numpy as np
def average(list):
    Output=sum(list)/len(list)
    return Output
def funkcija(f, x):
    y=eval(f, {"x":x, "x**2":x*x, "x**3":x*x*x, "sin":np.sin, "cos":np.cos})
    return y
def derivacija_u_tocki_twostep(f, x):
    hlist=np.linspace(0.1, 100, 999)
    fprime0=[]
    for i in hlist:
        fprime2=funkcija(f, (x+i))
        fprime1=funkcija(f, x)
        fprime0.append((fprime2-fprime1)/i)
    fprimevalue=average(fprime0)
    return fprimevalue
def derivacija_u_tocki(f, x):
    hlist=np.linspace(0.1, 100, 999)
    fprime0=[]
    for i in hlist:
        fprime2=funkcija(f, (x+i))
        fprime1=funkcija(f, (x-i))
        fprime0.append((fprime2-fprime1)/(2*i))    
    fprimevalue=average(fprime0)
    return(fprimevalue)
def derivacija(f, a, b, koraci):
    hlist=np.linspace(a, b, koraci)
    fprime0=[]
    for i in hlist:
        fprime2=funkcija(f, (a+i))
        fprime1=funkcija(f, a)
        fprime0.append((fprime2-fprime1)/i)    
    return fprime0
def integracija_numericki(f, a, b, n):
    dx=(b-a)/n
    step=np.linspace(a, b, n)
    U=0
    L=0
    for argument in step:
        U=U+funkcija(f, argument)*dx
        L=L+funkcija(f, (argument-1))*dx
    print("Vrijednost integrala iznosi između {} i {}".format(L, U))
def integracija_trapezna(f, a, b, n):
    dx=(b-a)/n
    step=np.linspace(a, b, n)
    prevalue=0
    for argument in step:
        prevalue=prevalue+(funkcija(f, argument))
    value=dx*(prevalue+(funkcija(f, b)-funkcija(f, a))/2)
    return value