import math
from functools import partial
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
op = None
num_1 = 0
num_2 = 0   
def num(x):
    text = main_window.lineEdit.text()
    main_window.lineEdit.setText(text + x)

def ac():
    main_window.lineEdit.setText("")

def c():
    t = main_window.lineEdit.text()
    main_window.lineEdit.setText(t[:-1])

def dot():
    if "." not in main_window.lineEdit.text():
        main_window.lineEdit.setText(main_window.lineEdit.text() + ".")

def sum():
    global op , num_1
    op = "+"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    
def sub(): 
    global op , num_1
    op = "-"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def mul():
    global op , num_1
    op = "*"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def div():
    global op , num_1
    op = "/"
    num_1 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")

def sin():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.sin(num)))

def cos():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.cos(num)))

def tan():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.tan(num)))

def cot():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.cos(math.radians(num) / math.sin(math.radians(num)))))

def pi():
    text = main_window.lineEdit.text()
    main_window.lineEdit.setText(text + "3.14")

def pow():
    text = float(main_window.lineEdit.text())
    text2 = text ** 2
    main_window.lineEdit.setText(str(text2))

def log():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.log(num)))

def fuc():
    num = int(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.factorial(num)))

def sqrt():
    num = float(main_window.lineEdit.text())
    main_window.lineEdit.setText(str(math.sqrt(num)))

def abs():
    num_1 = float(main_window.lineEdit.text())
    abc = num_1 * -1
    main_window.lineEdit.setText(str(abc))

def equal():
    if op == "+":
        eq_sum()
    elif op == "-":
        eq_sub()
    elif op == "*":
        eq_mul()
    elif op == "/":
        eq_div()
def eq_sum():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 + num_2
    main_window.lineEdit.setText(str(result))
def eq_sub():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 - num_2
    main_window.lineEdit.setText(str(result))

def eq_mul():
    num_2 = float(main_window.lineEdit.text())
    main_window.lineEdit.setText("")
    result = num_1 * num_2
    main_window.lineEdit.setText(str(result))

def eq_div():
    try:
        num_2 = float(main_window.lineEdit.text())
        main_window.lineEdit.setText("")
        result = num_1 / num_2
        main_window.lineEdit.setText(str(result))
    except:
        main_window.lineEdit.setText("you can not divition by zero!")

app = QApplication([])
loader = QUiLoader()

main_window = loader.load("calculator.ui")
main_window.show()

main_window.btn_c.clicked.connect(c)
main_window.btn_0.clicked.connect(partial(num, "0"))
main_window.btn_1.clicked.connect(partial(num, "1"))
main_window.btn_2.clicked.connect(partial(num, "2"))
main_window.btn_3.clicked.connect(partial(num, "3"))
main_window.btn_4.clicked.connect(partial(num, "4"))
main_window.btn_5.clicked.connect(partial(num, "5"))
main_window.btn_6.clicked.connect(partial(num, "6"))
main_window.btn_7.clicked.connect(partial(num, "7"))
main_window.btn_8.clicked.connect(partial(num, "8"))
main_window.btn_9.clicked.connect(partial(num, "9"))
main_window.btn_sum.clicked.connect(sum)
main_window.btn_sub.clicked.connect(sub)
main_window.btn_mul.clicked.connect(mul)
main_window.btn_div.clicked.connect(div)
main_window.btn_sin.clicked.connect(sin)
main_window.btn_cos.clicked.connect(cos)
main_window.btn_log.clicked.connect(log)
main_window.btn_tan.clicked.connect(tan)
main_window.btn_sqrt.clicked.connect(sqrt)
main_window.btn_cot.clicked.connect(cot)
main_window.btn_dot.clicked.connect(dot)
main_window.btn_equal.clicked.connect(equal)


app.exec()