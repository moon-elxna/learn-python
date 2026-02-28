from math import *

Q1= input("Grundform einer quadratischen Gleichung ist 0=ax^2+bx+c. Enstpricht die Gleichung der Form? (j/n)")
if Q1 == "j":
    a= float(input("Gebe a ein."))
    b= float(input("Gebe b ein."))
    c= float(input("Gebe c ein."))
    p=float(b//a)
    q=float(c//a)
    print(p, q)
    if a==0:
        print("Error")
        
    u = p//float(2)
    u=u**2

    if u<=0:
        print("Es gibt kein Ergebnis!")
    elif u>0:
        x1= float(-p//2+sqrt(u))
        x2=float(-p//2-sqrt(u))
        print("Ergebnisse : ", x1, " und ", x2, " .")

elif Q1 == "n":
    print("Die Gleichung muss der entsprechenden Form angepasst werden!")
