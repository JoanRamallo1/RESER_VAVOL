class Cars:

    def __init__(self):
        self.code = []
        self.Marca = []
        self.LlocRecollida = []
        self.Price = []
        """Numero de dies"""
        self.Durada = []
    
    
    def add_car(self, code, marca = [], LlocRecollida = [], Price = 0, durada = 0):
        self.code.append(code)
        self.Marca.append(marca)
        self.LlocRecollida.append(LlocRecollida)
        self.Price.append(Price)
        self.Durada.append(durada)
        
    def get_price_cars(self):
        sum = 0
        for i in self.Price:
            sum = sum + i
        return sum
    
    
    def del_car(self, code):
        if code in self.code:
            i = self.code.index(code)
            self.code.pop(i)
            self.Marca.pop(i)
            self.LlocRecollida.pop(i)
            self.Price.pop(i)
            self.Durada.pop(i)