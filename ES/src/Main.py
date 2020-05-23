from src.Flights import Flights
from src.Bank import Bank
from src.User import User
from src.Booking import Booking
from src.Cars import Cars
from src.Hotels import Hotels
from src.PaymentData import PaymentData
from src.Rentalcars import Rentalcars
from src.Skyscanner import Skyscanner


class Reserva:
    
    
    def __init__(self):
        self.flights = Flights()
        self.bank = Bank()
        self.user = User()
        self.booking = Booking()
        self.cars = Cars()
        self.hotels = Hotels()
        self.paymentdata = PaymentData()
        self.rentalcars = Rentalcars()
        self.skyscanner = Skyscanner()
        pass
    
    def get_TOTAL_preu(self):
        sum = self.flights.getPrice() + self.cars.get_price_cars() + self.hotels.get_price_habitacions()
        return sum
    
    """VUELOS"""
    
    def getCodi(self):
        return self.flights.getCodi()
    
    def getPrice(self):
        return self.flights.getPrice()
    
    def getDestination(self):
        return self.flights.getDestination()
    
    def getNumPassangers(self):
        return self.flights.getNumPassangers()
    
    def getTotalPrice(self):
        return self.flights.getTotalPrice()
    
    def add_destination(self, destination):
        self.flights.add_destination(destination)
        
    def del_destination(self, destination):
        self.flights.del_destination(destination)
        
    def add_Passanger(self, numero):
        self.flights.add_Passanger(numero)
    
        
    """BANCO"""
    
    def do_payment(self):
        return self.bank.do_payment(self.user, self.paymentdata)
    
    
    """SKYSCANNER"""
    
    def confirm_reserve(self):
        return self.skyscanner.confirm_reserve(self.user, self.flights)
    """BOOKING"""
    
    def confirm_reserve1(self):
        return self.booking.confirm_reserve1(self.user, self.flights)
    
    """RENTALCARS"""
    
    def confirm_reserve2(self):
        return self.rentalcars.confirm_reserve2(self.user, self.flights)
    
    """PAYMENTDATA"""
    def add_dades (self, Nombre, a1, a2, Numero, Codi):
        return self.paymentdata.add_dades( Nombre, a1, a2, Numero, Codi)
    
    def add_import(self, Import):
        return self.paymentdata.add_import(Import)
    
    def add_Targeta(self, Targeta):
        return self.paymentdata.add_Targeta(Targeta)
    
    def get_Targeta(self):
        return self.paymentdata.get_Targeta()
        
    """USER"""
    
    def Insert_User_Data(self, DNI, name, a1, a2, phone, email, sex, nacionality, birthdate):
        return self.user.Insert_User_Data(DNI, name, a1, a2, phone, email, sex, nacionality, birthdate)
    
    """Cars"""
    
    def add_car(self, code):
        self.cars.add_car(code)
    
    def get_price_cars(self):
        return self.cars.get_price_cars()
        
    def del_car(self, code):
        self.cars.del_car(code)
    
    
    """Hotels"""
        
    def add_Hotel(self, nom):
        self.hotels.add_Hotel(nom)
        
    def get_price_habitacions(self):
        return self.hotels.get_price_habitacions()
         
    def del_hotel(self, nom):
        self.hotels.del_hotel(nom)
        
        
        
        
        
        
        
        