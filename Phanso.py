class Phanso():
    def __init__(self, tuso, mauso):
        self.tuso = tuso
        self.mauso = mauso
    
    def cong(self, phanso):
        if self.mauso == phanso.mauso:
            result = Phanso(self.tuso + phanso.tuso, self.mauso)
            result.print_phanso()
        else:
            tusomoi = self.tuso * phanso.mauso
            mausomoi = self.mauso * phanso.mauso
            tusomoi1 = phanso.tuso * self.mauso
            mausomoi1 = phanso.mauso * self.mauso
            result = Phanso(tusomoi + tusomoi1, mausomoi)
            result.print_phanso()
    
    def tru(self, phanso):
        if self.mauso == phanso.mauso:
            result = Phanso(self.tuso - phanso.tuso, self.mauso)
            result.print_phanso()
            
        else:
            tusomoi = self.tuso * phanso.mauso
            mausomoi = self.mauso * phanso.mauso
            tusomoi1 = phanso.tuso * self.mauso
            mausomoi1 = phanso.mauso * self.mauso
            result = Phanso(tusomoi - tusomoi1, mausomoi)
            result.print_phanso()

    
    def nhan(self, phanso):
        result1 = Phanso(self.tuso*phanso.tuso, self.mauso*phanso.mauso)
        result1.print_phanso()
    
    def chia(self, phanso):
        result2 = Phanso(self.tuso*phanso.mauso, self.mauso*phanso.tuso)
        result2.print_phanso()

    def print_phanso(self):
        print(f"Tu so {self.tuso} mau so {self.mauso}")
    
phanso1 = Phanso(3,5)
phanso2 = Phanso(2,6)
phanso1.tru(phanso2)