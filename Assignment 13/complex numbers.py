num_a1 = float(input("enter your firs number : "))
num_b1 = float(input("enter your second number  : "))
num_a2 = float(input("enter your first number : "))
num_b2 = float(input("enter your second number : "))

dict_numbers = {"a1": num_a1, "b1": num_b1, "a2": num_a2, "b2": num_b2} 

def sum(dict_numbers):
    return f"{dict_numbers['a1'] + dict_numbers['a2']}, {dict_numbers['b1'] + dict_numbers['b2']}"

def sub(dict_numbers):
    return f"{dict_numbers['a1'] - dict_numbers['a2']}, {dict_numbers['b1'] - dict_numbers['b2']}"

operation = int(input("""1 = sum
2 = sub\n"""))

if operation == 1:
    print(sum(dict_numbers))
elif operation == 2:
    print(sub(dict_numbers))