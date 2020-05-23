class Flights:

    def __init__(self):
        self.Destination = []
        self.Num_passangers = 0
        self.Codi = []
        self.Price = []
        
    def getCodi(self):
        return self.Codi
    
    def getPrice(self):
        return self.Price
    
    def getDestination(self):
        return self.Destination
    
    def getNumPassangers(self):
        return self.Num_passangers
    
    def getTotalPrice(self):
        sum = 0
        for i in self.Price:
            sum = sum + i
        return sum * self.Num_passangers
    def add_destination(self, destination, codi = 0, preu = 0):
        self.Destination.append(destination)
        self.Codi.append(codi)
        self.Price.append(preu)
        
    def add_Passanger(self, numero):
        self.Num_passangers = numero
        
    def del_destination(self, destination):
        if destination in self.Destination:
            i = self.Destination.index(destination)
            self.Destination.pop(i)
            self.Codi.pop(i)
            self.Price.pop(i)
        pass