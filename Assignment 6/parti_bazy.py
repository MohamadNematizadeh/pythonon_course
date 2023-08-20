list = ['Milad','Ahmad','Mohammad','Saeed','Ali']

print('safe nanvaiee =',list)

na1 = str(input('enter name : '))
na2 = int(input('enter place : '))

new_na1 = str(input('enter name : '))
new_na2 = int(input('enter place : '))

my_na1 = str(input('enter name : '))
my_na2 = int(input('enter place : '))

list.insert(na2,na1)
list.insert(new_na2,new_na1)
list.insert(my_na2,my_na1)

print(list)