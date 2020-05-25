
import unittest
from src.Main import Reserva
from unittest import mock

class TestBank(unittest.TestCase):
    @mock.patch('src.Flights.Flights.getTotalPrice')
    def test_1_12(self, mock_preu):
        res = Reserva()
        res.add_dades('Robert', 'Norman', 'Ross', [1234,1234,1234], 123)
        res.add_destination('Españita')
        res.add_destination('Roma')
        res.add_Passanger(4)
        mock_preu.return_value = 50
        preu = res.getTotalPrice()
        res.add_import(preu)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        self.assertEqual(res.do_payment(), True)
        
        
    @mock.patch('src.Flights.Flights.getTotalPrice')
    def test_2_1(self, mock_preu):
        res = Reserva()
        res.add_dades('Robert', 'Norman', 'Ross', [1234,1234,1234], 123)
        res.add_destination('Españita')
        res.add_destination('Roma')
        res.add_Passanger(4)
        res.add_Targeta('Visa')
        self.assertEqual(res.get_Targeta(), 'Visa')
        mock_preu.return_value = 50
        preu = res.getTotalPrice()
        res.add_import(preu)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        self.assertEqual(res.do_payment(), True)  
    
    @mock.patch('src.Bank.Bank.do_payment')
    def test_2_2(self, mock_payment):
        mock_payment.return_value = False
        res = Reserva()
        res.add_dades('Robert', 'Norman', 'Ross', [1234,1234,1234], 123)
        res.add_destination('Españita')
        res.add_destination('Roma')
        res.add_Passanger(4)       
        preu = res.getTotalPrice()
        res.add_import(preu)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        self.assertEqual(res.do_payment(), False)  
    
    
    
if __name__ == '__main__':
    unittest.main(exit=False)
    
    