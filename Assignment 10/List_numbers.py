numbers_str = input("yoru enter numbers: ")
numbers_int = int(input("yoru enter other numbers: "))

numbers_str_dict = {}
numbers_int_dict = {"0": 0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}

for number in numbers_str:
    if number in numbers_str_dict:
        numbers_str_dict[number] += 1
    else:
        numbers_str_dict[number] = 1
print("dictionary number:", numbers_str_dict)

numbers_list = []
for i in str(numbers_int):
    if str(i) in str(numbers_int):
        numbers_int_dict[str(i)] += 1
        if str(i) not in numbers_list:
            numbers_list.append(str(i))
print("list number : ", end="")

for j in numbers_list:
    print(j, ":", numbers_int_dict[j], "|", end="")

print()