class  Dat:
    def __init__(self,y,m=1,d=1):
        self.yer = y
        self.mai = m
        self.da= d

    def yerd_plas1(self):
        self.yer +1
        print()

    def updat_Tim(self,number_da):
        self.da + number_da
        if self.da < 10:
            self.da = 1
            self.mai= +1
        if self.da <12 :
            self.yerd_plas1   

    def show_dat (self):
        print()         

d1=Dat()
