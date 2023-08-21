time1 = input("enter your time (1): ") #2:12:123
time2 = input("enter your time (2): ")

def set_time (time):
    dict = time.split(":")
    time = {"h": int(dict[0]), "m": int(dict[1]), "s": int(dict[2])}
    return time 

def sum(time1, time2):
    time = {"h": time1["h"] + time2["h"] , "m": time1["m"] + time2["m"] , "s": time1["s"] + time2["s"] }
    time = check(time)
    return time

def sub(time1, time2): 
    time = {"h": time1["h"] - time2["h"] , "m": time1["m"] - time2["m"] , "s": time1["s"] - time2["s"] }
    time = check(time)
    return time
    
def check(time):
    while not(0 < time["s"] < 60 and 0 < time["m"] < 60):
        if time["s"] > 60:
            time["s"] -= 60
            time["m"] += 1
        
        elif time["s"] < 0:
            time["m"] -= 1
            time["s"] += 60 
        
        if time["m"] > 60:
            time["m"] -= 60
            time["h"] += 1

        elif time["m"] < 0:
            time["h"] -= 1
            time["m"] += 60

    return time

def show(time):
    print(f"{time['h']}:{time['m']}:{time['s']}")

time1 = set_time(time1)
time2 = set_time(time2)

op = int(input("""1 = sum
2 = sub\n"""))

if op == 1:
    x = sum(time1, time2)
    show(x)
elif op == 2:
    z = sub(time1, time2 )
    show(z)
else:
    print("your number is wrong")