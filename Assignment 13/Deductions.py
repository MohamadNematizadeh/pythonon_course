numerator1 = float(input("enter your first numerator: "))
denominator1 = float(input("enter your first denominator: "))
numerator2 = float(input("enter your second numerator: "))
denominator2 = float(input("enter your second denominator: "))

def set(numerator, denominator):
    deduction = {"s": numerator, "m": denominator}
    return deduction

def show(deduction):
    print("",deduction["s"],"\n ----\n" , deduction["m"]) 

def sum(deduction1, deduction2):
    deduction = {}
    deduction["s"] = (deduction1["s"] * deduction2["m"]) + (deduction2["s"] * deduction1["m"])
    deduction["m"] = deduction1["m"] * deduction2["m"]
    return deduction
    
def sub(deduction1, deduction2):
    deduction = {}
    deduction["s"] = (deduction1["s"] * deduction2["m"]) - (deduction2["s"] * deduction1["m"])
    deduction["m"] = deduction1["m"] * deduction2["m"]
    return deduction

def mul(deduction1, deduction2):
    deduction = {}
    deduction["s"] = deduction1["s"] * deduction2["s"] 
    deduction["m"] = deduction1["m"] * deduction2["m"] 
    return deduction

def div(deduction1, deduction2):
    deduction = {}
    deduction["s"] = deduction1["s"] * deduction2["m"]
    deduction["m"] = deduction1["m"] * deduction2["s"]
    return deduction

deduction1 = set(numerator1, denominator1)
deduction2 = set(numerator2, denominator2)

op = int(input("""1 = sum
2 = sub
3 = mul
4 = div\n"""))

if op == 1:
    x = sum(deduction1, deduction2 )
    show(x)

elif op == 2:
    x = sub(deduction1, deduction2 )
    show(x)

elif op == 3:
    x = mul(deduction1, deduction2 )
    show(x)

elif op == 4:
    x = div(deduction1, deduction2 )
    show(x)

else:
    print("your number is wrong")
    