class Time:
    def __init__(self, h, m, s, h2, m2, s2):
        self.h = h
        self.m = m
        self.s = s
        self.h2 = h2
        self.m2 = m2
        self.s2 = s2
    def sum(self):
        hour_s = self.h + self.h2
        minut_s = self.m + self.m2
        second_s = self.s + self.s2
        while not(0 <= second_s <= 60 and 0 <= minut_s <= 60):
            if second_s >= 60:
                second_s -= ((second_s // 60) * 60)
                minut_s += (second_s // 60)
            if minut_s >= 60:
                minut_s -= ((minut_s // 60) * 60)
                hour_s += (minut_s // 60)
        print(str(hour_s) + ":" + str(minut_s)  + ":" + str(second_s))
    def sub(self):
        hour_m = self.h - self.h2
        minut_m = self.m - self.m2
        second_m = self.s - self.s2
        while not(0 <= second_m <= 60 and 0 <= minut_m <= 60):
            if second_m < 0:
                minut_m -= 1
                second_m += 60
            if minut_m < 0:
                hour_m -= 1
                minut_m += 60
        print(str(hour_m) + ":" + str(minut_m)  + ":" + str(second_m))
t = input("enter time1:for exampel (20:45:30)\n")
t2 = input("enter time2:for exampel (20:45:30)\n")
op = int(input("1_sub\n2_sum\nenter number of your choice: "))
t = t.split(":")
t = [eval(i) for i in t]
t2 = t2.split(":")
t2 = [eval(i) for i in t2]
time = Time(t[0], t[1], t[2], t2[0], t2[1], t2[2])
if op == 1:
    time.sub()
else:
    # time.sum()
