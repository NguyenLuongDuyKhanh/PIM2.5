class Phanso():
    def __init__(self,tuso,mauso):
        self.tuso = tuso
        self.mauso = mauso
    
    def nhan(self,phanso):
        result = Phanso(self.tuso*phanso.tuso,self.mauso*phanso.mauso)
        result.print_phanso()

    def chia(self,phanso):
        result = Phanso(self.mauso*phanso.tuso,self.tuso*phanso.mauso)
        result.print_phanso()

    def cong(self,phanso):
        if self.mauso == phanso.mauso:
            result = Phanso(self.mauso+phanso.mauso,self.mauso)
            result.print_phanso()
        elif self.mauso % phanso.mauso == 0:
            #mauso_b =  self.mauso/phanso.mauso * phanso.mauso
            tuso_b = self.mauso/phanso.mauso * phanso.tuso
            result = Phanso(tuso_b+self.tuso,self.mauso)
            result.print_phanso()
        elif phanso.mauso % self.mauso == 0:
            #mauso_b =  self.mauso/phanso.mauso * phanso.mauso
            tuso_a = phanso.mauso/self.mauso * self.tuso
            result = Phanso(tuso_a+phanso.tuso,phanso.mauso)
            result.print_phanso()
        elif self.mauso != phanso.mauso:
            mauso_a = self.mauso*phanso.mauso
            tuso_a = self.tuso*phanso.mauso
            mauso_b =  mauso_a
            tuso_b = phanso.tuso*self.mauso
            result = Phanso(tuso_b+tuso_a,mauso_b)
            result.print_phanso()

    def tru(self,phanso):
        print("da goi")
        if self.mauso == phanso.mauso:
            result = Phanso(self.tuso-phanso.tuso,self.mauso)
            result.print_phanso()
        elif self.mauso % phanso.mauso == 0:
            tuso_b = self.mauso/phanso.mauso * phanso.tuso
            print(tuso_b)
            result = Phanso(self.tuso-tuso_b,self.mauso)
            result.print_phanso()
        elif phanso.mauso % self.mauso == 0:
            #mauso_b =  self.mauso/phanso.mauso * phanso.mauso
            tuso_a = phanso.mauso/self.mauso * self.tuso
            result = Phanso(tuso_a-phanso.tuso,phanso.mauso)
            result.print_phanso()
        elif self.mauso != phanso.mauso:
            mauso_a = self.mauso*phanso.mauso
            tuso_a = self.tuso*phanso.mauso
            mauso_b =  mauso_a
            tuso_b = phanso.tuso*self.mauso
            result = Phanso(tuso_a-tuso_b,mauso_b)
            result.print_phanso()


    def print_phanso(self):
        print(f"Tu so {self.tuso} mauso {self.mauso}")


a = Phanso(10,3)
b = Phanso(4,4)


b.tru(a)
