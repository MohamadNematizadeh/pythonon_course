from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication([])
loder = QUiLoader()
Home = loder.load("Home.ui")
Home.show()
main_window = loder.load("main.ui")

def Fahrenheit_to_Celsius():
    def f_c_set(n, u, c):
        main_window.unit_show.setText("Fahrenheit")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) -32
        result = result / 1.8

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Fahrenheit_to_Celsius.isChecked():

        f_c_set("0", "Fahrenheit", "Celsius")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_c_set, "-1", "Fahrenheit", "Celsius"))

def Celsius_to_Kelvin():
    def s_k_set(n, u, c):
        main_window.unit_show.setText("Celsius")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) + 273.15

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Celsius_to_Kelvin.isChecked():
        s_k_set("0", "Celsius", "Kelvin")
        main_window.show()

        main_window.convert.clicked.connect(partial(s_k_set, "-1", "Celsius", "Kelvin"))

def Fahrenheit_to_Kelvin():
    def f_k_set(n, u, c):
        main_window.unit_show.setText("Fahrenheit")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) + 459.67
        result /= 9
        result *= 5

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Fahrenheit_to_Kelvin.isChecked():
        f_k_set("0", "Fahrenheit", "Kelvin")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_k_set, "-1", "Fahrenheit", "Kelvin"))

def Kelvin_to_Celsius():
    def k_c_set(n, u, c):
        main_window.unit_show.setText("Kelvin")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) - 273.15

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Kelvin_to_Celsius.isChecked():
        k_c_set("0", "Kelvin", "Celsius")
        main_window.show()

        main_window.convert.clicked.connect(partial(k_c_set, "-1", "Kelvin", "Celsius"))

def Foot_to_Inch():
    def f_i_set(n, u, c):
        main_window.unit_show.setText("Foot")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 12

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Foot_to_Inch.isChecked():
        f_i_set("0", "Foot", "Inch")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_i_set, "-1", "Foot", "Inch"))

def Foot_to_Centimeter():
    def f_c_set(n, u, c):
        main_window.unit_show.setText("Foot")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 30.5

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Foot_to_Centimeter.isChecked():
        f_c_set("0", "Foot", "Centimeter")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_c_set, "-1", "Foot", "Centimeter"))

def Foot_to_Meter():
    def f_m_set(n, u, c):
        main_window.unit_show.setText("Foot")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 0.305

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Foot_to_Meter.isChecked():
        f_m_set("0", "Foot", "Meter")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_m_set, "-1", "Foot", "Meter"))

def Foot_to_Yard():
    def f_y_set(n, u, c):
        main_window.unit_show.setText("Foot")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 0.333

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Foot_to_Yard.isChecked():
        f_y_set("0", "Foot", "Yard")
        main_window.show()

        main_window.convert.clicked.connect(partial(f_y_set, "-1", "Foot", "Yard"))

def Euro_to_USD():
    def e_u_set(n, u, c):
        main_window.unit_show.setText("Euro")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 1.080900

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Euro_to_USD.isChecked():
        e_u_set("0", "Euro", "USD")
        main_window.show()

        main_window.convert.clicked.connect(partial(e_u_set, "-1", "Euro", "USD"))

def Euro_to_Cad():
    def e_c_set(n, u, c):
        main_window.unit_show.setText("Euro")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 1.467070

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Euro_to_Cad.isChecked():
        e_c_set("0", "Euro", "Cad")
        main_window.show()

        main_window.convert.clicked.connect(partial(e_c_set, "-1", "Euro", "Cad"))

def Euro_to_Tnd():
    def e_t_set(n, u, c):
        main_window.unit_show.setText("Euro")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 3.474156

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Euro_to_Tnd.isChecked():
        e_t_set("0", "Euro", "Tnd")
        main_window.show()

        main_window.convert.clicked.connect(partial(e_t_set, "-1", "Euro", "Tnd"))

def Euro_to_Cnh():
    def e_c_set(n, u, c):
        main_window.unit_show.setText("Euro")
        if n != "-1":
            main_window.unit_line.setText(n)

        result = float(main_window.unit_line.text()) * 7.869739

        main_window.eql.setText(f"{u} -> {main_window.unit_line.text()} = {c} -> {result}")

    if Home.Euro_to_Cnh.isChecked():
        e_c_set("0", "Euro", "Cnh")
        main_window.show()

        main_window.convert.clicked.connect(partial(e_c_set, "-1", "Euro", "Cnh"))

Home.Fahrenheit_to_Celsius.toggled.connect(Fahrenheit_to_Celsius)
Home.Fahrenheit_to_Kelvin.toggled.connect(Fahrenheit_to_Kelvin)
Home.Celsius_to_Kelvin.toggled.connect(Celsius_to_Kelvin)
Home.Kelvin_to_Celsius.toggled.connect(Kelvin_to_Celsius)
Home.Foot_to_Inch.toggled.connect(Foot_to_Inch)
Home.Foot_to_Centimeter.toggled.connect(Foot_to_Centimeter)
Home.Foot_to_Meter.toggled.connect(Foot_to_Meter)
Home.Foot_to_Yard.toggled.connect(Foot_to_Yard)
Home.Euro_to_USD.toggled.connect(Euro_to_USD)
Home.Euro_to_Cad.toggled.connect(Euro_to_Cad)
Home.Euro_to_Tnd.toggled.connect(Euro_to_Tnd)
Home.Euro_to_Cnh.toggled.connect(Euro_to_Cnh)

app.exec_()