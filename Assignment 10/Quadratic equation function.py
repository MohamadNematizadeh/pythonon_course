import math
def e_2nd_d(a, b, c):
    d = (b**2) - (4*a*c)
    if d > 0:
        sol1 = (-b-math.sqrt(d))/(2*a)
        sol2 = (-b+math.sqrt(d))/(2*a)
        return sol1, sol2
    elif d == 0:
        sol3 = (-b / (a ** 2))
        return sol3
    else:
        return None
    
a = int(input("enter a: "))
b = int(input("enter b: "))
c = int(input("enter c: "))
print(e_2nd_d(a, b, c))