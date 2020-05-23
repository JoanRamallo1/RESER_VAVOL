class PaymentData:

    def __init__(self):
        self.Targeta = ' '
        self.Titular = ' '
        self.Numero = [0000,0000,0000]
        self.Codi = 0
        self.Import = 0
    
    def add_dades (self, Nombre, a1, a2, Numero, Codi):
        self.Nombre = Nombre
        self.Apellido1 = a1
        self.Apellido2 = a2
        self.Numero = Numero
        self.Codi =Codi
    
    def add_import(self, Import):
        self.Import = Import
        
    def add_Targeta(self, Targeta):
        self.Targeta = Targeta
        
    def get_Targeta(self):
        return self.Targeta
        pass