number = int(input('input your number: '))
number = str(number)
b = 0
c = 0
if number.count('0') != 0:
    b += number.count('0')
if number.count('2') != 0:
    b += number.count('2')
if number.count('4') != 0:
    b += number.count('4')
if number.count('6') != 0:
    b += number.count('6')
if number.count('8') != 0:
    b += number.count('8')
if number.count('1') != 0:
    c += number.count('1')
if number.count('3') != 0:
    c += number.count('3')
if number.count('5') != 0:
    c += number.count('5')
if number.count('7') != 0:
    c += number.count('7')
if number.count('9') != 0:
    c += number.count('9')
if b > c :
    print('zoj')
elif c>b:
    print('fard')
else:
    print('=')