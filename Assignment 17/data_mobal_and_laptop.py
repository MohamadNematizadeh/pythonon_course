import sqlite3
import csv

data = sqlite3.connect("Data/data_mobal_and_laptop.db")
c = data.cursor()
laptops = []
with open("Data/Mobal_labtab.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        laptops.append(tuple(row))

try:
    c.execute("""
    CREATE TABLE mobile (
        brand TEXT,
        name TEXT,
        year INT,
        ram TEXT,
        camera TEXT,
        price INT
    )
""")
except:
    pass
try:
    c.execute("""
    CREATE TABLE laptop (
        brand TEXT,
        Brand TEXT,
        CPU TEXT,
        RAM TEXT,
        ssd TEXT,
        hdd TEXT,
        GPU TEXT,
        Op_System TEXT,
        Weight TEXT,
        Price INT
    )
""")
except:
    pass

mobiles = [("Apple", "iPad Pro 12.9 (2018)", "2018", "4 GB", "12 MP", "1100"),
            ("Apple", "iPad Pro 11", "2018", "4 GB", "12 MP", "880"),
            ("Apple", "iPhone XS Max", "2018", "4 GB", "12 MP", "1250"),
            ("Apple", "iPhone XS", "2018", "4 GB", "12 MP", "1150"),
            ("Apple", "iPhone XR", "2018", "3 GB", "12 MP", "850"),
            ("Apple", "Watch Series 4", "2018", "0 GB", "No", "700"),
            ("Apple", "Watch Series 4 Aluminum", "2018", "0 GB", "No", "430"),
            ("Apple", "iPad 9.7 (2018)", "2018", "2 GB", "8 MP", "350"),
            ("Apple", "iPhone X", "2017", "3 GB", "12 MP", "1000"),
            ("Apple", "iPhone 8 Plus", "2017", "3 GB", "12 MP", "770"),
            ("Apple", "iPhone 8", "2017", "2 GB", "12 MP", "700"),
            ("Apple", "Watch Edition Series 3", "2017", "0.768 GB", "No", "1450"),
            ("Apple", "Watch Series 3", "2017", "0.768 GB", "No", "700"),
            ("Apple", "Watch Series 3 Aluminum", "2017", "0.768 GB", "No", "480"),
            ("Apple", "iPad Pro 12.9 (2018)", "2018", "4 GB", "12 MP", "1100"),
            ("Apple", "iPad Pro 11", "2018", "4 GB", "12 MP", "880"),
            ("Apple", "iPhone XS Max", "2018", "4 GB", "12 MP", "1250"),
            ("Apple", "iPhone XS", "2018", "4 GB", "12 MP", "1150"),
            ("Apple", "iPhone XR", "2018", "3 GB", "12 MP", "850"),
            ("Apple", "Watch Series 4", "2018", "0 GB", "No", "700"),
            ("Apple", "Watch Series 4 Aluminum", "2018", "0 GB", "No", "430"),
            ("Apple", "iPad 9.7 (2018)", "2018", "2 GB", "8 MP", "350"),
            ("Apple", "iPhone X", "2017", "3 GB", "12 MP", "1000"),
            ("Apple", "iPhone 8 Plus", "2017", "3 GB", "12 MP", "770"),
            ("Apple", "iPhone 8", "2017", "2 GB", "12 MP", "700"),
            ("Apple", "Watch Edition Series 3", "2017", "0.768 GB", "No", "1450"),
            ("Apple", "Watch Series 3", "2017", "0.768 GB", "No", "700"),
            ("Apple", "Watch Series 3 Aluminum", "2017", "0.768 GB", "No", "480"),
            ("Apple", "iPad Pro 12.9 (2017)", "2017", "4 GB", "12 MP", "900"),
            ("Apple", "iPad Pro 10.5 (2017)", "2017", "4 GB", "12 MP", "730"),
            ("Apple", "iPad 9.7 (2017)", "2017", "2 GB", "8 MP", "390"),
            ("Apple", "Watch Edition Series 2 42mm", "2016", "0.512 GB", "No", "1500"),
            ("Apple", "Watch Series 2 42mm", "2016", "0.512 GB", "No", "700"),
            ("Apple", "Watch Edition Series 2 38mm", "2016", "0.512 GB", "No", "1450"),
            ("Apple", "Watch Series 2 38mm", "2016", "0.512 GB", "No", "650"),
            ("Apple", "Watch Series 2 Aluminum 42mm", "2016", "0.512 GB", "No", "450"),
            ("Apple", "Watch Series 1 Aluminum 42mm", "2016", "0.512 GB", "No", "300"),
            ("Apple", "Watch Series 2 Aluminum 38mm", "2016", "0.512 GB", "No", "420"),
            ("Apple", "Watch Series 1 Aluminum 38mm", "2016", "0.512 GB", "No", "270"),
            ("Apple", "iPhone 7 Plus", "2016", "3 GB", "12 MP", "690"),
            ("Apple", "iPhone 7", "2016", "2 GB", "12 MP", "550"),
            ("Apple", "iPad Pro 9.7 (2016)", "2016", "2 GB", "12 MP", "690"),
            ("Apple", "iPhone SE", "2016", "2 GB", "12 MP", "300"),
            ("Apple", "iPhone 6s Plus", "2015", "2 GB", "12 MP", "470"),
            ("Apple", "iPhone 6s", "2015", "2 GB", "12 MP", "500"),
            ("Apple", "iPad Pro 12.9 (2015)", "2015", "4 GB", "8 MP", "850"),
            ("Apple", "iPad mini 4.1", "2015", "2 GB", "8 MP", "3360"),
            ("Apple", "Watch Edition 42mm (1st gen)", "2014", "0.512 GB", "No", "13000"),
            ("Apple", "Watch Edition 38mm (1st gen)", "2014", "0.512 GB", "No", "11000"),
            ("Apple", "Watch 42mm (1st gen)", "2014", "0.512 GB", "No", "700"),
            ("Apple", "Watch 38mm (1st gen)", "2014", "0.512 GB", "No", "650"),
            ("Apple", "Watch Sport 42mm (1st gen)", "2014", "0.512 GB", "No", "250"),
            ("Apple", "Watch Sport 38mm (1st gen)", "2014", "0.512 GB", "No", "250"),
            ("Apple", "iPad Air 2", "2014", "2 GB", "8 MP", "440"),
            ('Apple', 'iPhone 14 Plus', "2022", '6 GB', "120p", '4000'),
            ('Apple', 'iPhone 14 Pro Max', "2022", '6 GB', '1080p', '5900'),
            ('Apple', 'iPhone 13 mini', "2021", '4 GB','1080p', '5000'),
            ('Apple', 'iPhone 11 Pro', "2019", '4 GB', '1080p', '4500')]

for i in mobiles:
    c.execute("INSERT INTO mobile VALUES (?, ?, ?, ?, ?, ?)", i)

for i in laptops:
    c.execute("INSERT INTO laptop VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", i)


def Show_mobile_phones_before_2020(c):
    for i in c.execute("SELECT * FROM mobile WHERE year < 2020"):
        print(f"{i[0]}, {i[1]}, {i[5]}")
    
def mobiles_and_laptop_above_5000(c):
    print("Mobile prices above 50 tomans")
    for i in c.execute("SELECT * FROM laptop WHERE price > 5000"):
        print(i)
    print("--------------------------------------------------------")
    print("Laptop prices above 50 tomans")
    for i in c.execute("SELECT * FROM mobile WHERE price > 5000"):
        print(i)

def Show_5_laptops_with_the_most_amount_of_ssd(c):
    for i in zip(c.execute("SELECT * FROM laptop ORDER BY ssd"), range(5)):
        print(i[0])

while True:
    op = int(input(" 1= Show_mobile_phones_before_2020\n 2= Showing_laptop_and_mobile_above_5000_tomans\n 3= Show_5_laptops_with_the_most_amount_of_ssd\n 4= Exit and save\n "))
    if op == 1:
        Show_mobile_phones_before_2020(c)
    elif op == 2:
        mobiles_and_laptop_above_5000(c)
    elif op == 3:
        Show_5_laptops_with_the_most_amount_of_ssd(c)
    elif op == 4:
        break

data.commit()
data.close()