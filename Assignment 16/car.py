# import csv
import pandas as pd
import json

data = pd.read_csv("data/cars_dataset.csv")

class Car:
    def __init__(self, data):
        self.data = data

    def show_japanese_cars(self):
        japanese_cars = []
        cars = self.data.query("Origin == 'Japan'")["Car"]
        for i in cars:
            japanese_cars.append(i)

        return japanese_cars

    def longest_name(self):
        l = ""
        for i in self.data["Car"]:
            if len(i) > len(l):
                l = i
        
        return l

    def shortest_name(self):
        l = self.longest_name()
        for i in self.data["Car"]:
            if len(i) < len(l):
                l = i
        
        return l

    def average_cylinders(self):
        c = []
        for i in self.data["Cylinders"]:
            c.append(int(i))
        
        return sum(c) / len(c)

    def average_horsepower(self):
        p = []
        for i in self.data["Horsepower"]:
            p.append(int(i))
        
        return sum(p) / len(p)

    def light_cars(self):
        weights = [float(i) for i in self.data["Weight"]]
        names = [i for i in self.data["Car"]]

        weights2 = sorted(weights)
        names2 = []

        for i in range(0, 50):
            for j in range(len(weights)):
                if weights2[i] == weights[j]:
                    names2.append(names[j])
                    break

        return names2

car = Car(data)
while True:
    op = int(input(" 1 = Show Japanese cars\n 2 = longest name\n 3 = shortest name\n 4 = Average cylinders\n 5 = average horsepower\n 6 = light cars\n 7= save to json\n 8= exit\n inter yor numbers:"))

    if op == 1:
        print(car.show_japanese_cars())
    
    elif op == 2:
        print(car.longest_name())
    
    elif op == 3:
        print(car.shortest_name())

    elif op == 4:
        print(car.average_cylinders())

    elif op == 5:
        print(car.average_horsepower())

    elif op == 6:
        print(car.light_cars())

    elif op == 7:
        data = {"japanese_cars":car.show_japanese_cars() ,
                "longest_name":car.longest_name(),
                "shortest_name":car.shortest_name(),
                "cylinders_average":car.average_cylinders(),
                "horsepower_average":car.average_horsepower(),
                "light_cars":car.light_cars()
                }

        d = open("cars_dataset.json", "w")
        json.dump(data, d)
        print("Complet teh file Json")
        d.close()
    
    elif op == 8:
        break