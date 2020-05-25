
import unittest
from src.Main import Reserva
from unittest import mock

class Testbooking(unittest.TestCase):
    
    @mock.patch('src.Booking.Booking.confirm_reserve1')    
    def test_3_7(self, mock_reserva):
        res = Reserva()
        res.add_destination('Roma')
        res.add_destination('Paris')
        res.add_destination('Españita')
        res.add_Passanger(4)
        res.add_car(0)
        res.add_car(0)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Pablo', 'Norman', 'Ross', 123456789, 'PabloRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Alberto', 'Norman', 'Ross', 123456789, 'AlbertoRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Pedro', 'Norman', 'Ross', 123456789, 'PedroRoss@hotmail.com', 'Male', 'American', 3)
        mock_reserva.return_value = True
        confirmacio = res.confirm_reserve1()
        self.assertEqual(confirmacio, True)
        
    @mock.patch('src.Booking.Booking.confirm_reserve1')   
    def test_3_8(self, mock_reserva):
        res = Reserva()
        res.add_destination('Roma')
        res.add_destination('Paris')
        res.add_destination('Españita')
        res.add_Passanger(4)
        res.add_car(0)
        res.add_car(0)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Pablo', 'Norman', 'Ross', 123456789, 'PabloRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Alberto', 'Norman', 'Ross', 123456789, 'AlbertoRoss@hotmail.com', 'Male', 'American', 3)
        res.Insert_User_Data('12345678A', 'Pedro', 'Norman', 'Ross', 123456789, 'PedroRoss@hotmail.com', 'Male', 'American', 3)
        mock_reserva.return_value = True
        confirmacio = res.confirm_reserve1()
        self.assertEqual(confirmacio, True)
    
if __name__ == '__main__':
    unittest.main(exit=False)