class Hotels:

    def __init__(self):
        self.code = []
        self.nom = []
        self.hostes = []
        self.habitacions = []
        """Numero de dies"""
        self.durada = []
        self.Price = []
    
    
    def add_Hotel(self, nom, code = 0, hostes = 0, habitacions = 0, durada = 0, price = 0):
        self.code.append(code)
        self.nom.append(nom)
        self.hostes.append(hostes)
        self.habitacions.append(habitacions)
        self.durada.append(durada)
        self.Price.append(price)
        
        
    def get_price_habitacions(self):
        sum = 0
        for i in self.Price:
            sum = sum + i
        return sum
    
    
    def del_hotel(self, nom):
        if nom in self.nom:
            i = self.nom.index(nom)
            self.code.pop(i)
            self.nom.pop(i)
            self.hostes.pop(i)
            self.habitacions.pop(i)
            self.durada.pop(i)
            self.Price.pop(i)
            