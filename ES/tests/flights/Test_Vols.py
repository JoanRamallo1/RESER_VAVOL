
import unittest
from src.Main import Reserva
from unittest import mock

class TestFlights(unittest.TestCase):

    def test_1_1(self):
        res = Reserva()
        res.add_destination('Roma')
        res.add_Passanger(2)
        self.assertEqual(res.getNumPassangers(), 2)

    def test_1_2(self):
        res = Reserva()
        self.assertEqual(res.getDestination(), [])
    def test_1_3(self):
        res = Reserva()
        self.assertEqual(res.getCodi(), [])
    def test_1_4(self):
        res = Reserva()
        self.assertEqual(res.getTotalPrice(), 0)
    def test_1_5(self):
        res = Reserva()
        res.add_destination('Españita')
        self.assertEqual(res.getDestination(), ['Españita'])
    
    @mock.patch('src.Flights.Flights.getCodi')
    def test_1_6(self, mock_codi):
        res = Reserva()
        """hacer mock para que el vuelo a españa tenga codigo 1"""
        res.add_destination('Españita')
        mock_codi.return_value = [1]
        self.assertEqual(res.getCodi(), [1])
    @mock.patch('src.Flights.Flights.getTotalPrice')
    def test_1_7(self, mock_preu):
        res = Reserva()
        """hacer mock para que el vuelo a españa tenga precio 3"""
        res.add_destination('Españita')
        res.add_Passanger(2)
        mock_preu.return_value = 6
        self.assertEqual(res.getTotalPrice(), 6)
        
    @mock.patch('src.Flights.Flights.getTotalPrice')
    def test_1_8(self, mock_preu):
        res = Reserva()
        """hacer mock para que el vuelo a españa tenga precio 3"""
        res.add_destination('Españita')
        """hacer mock para que el vuelo a roma tenga precio 2"""
        res.add_destination('Roma')
        res.add_Passanger(2)
        mock_preu.return_value = 10
        self.assertEqual(res.getTotalPrice(), 10)
        
    def test_1_9(self):
        res = Reserva()
        res.add_destination('Españita')
        res.add_destination('Roma')
        res.del_destination('Españita')
        self.assertEqual(res.getDestination(), ['Roma'])
    
    
    @mock.patch('src.Flights.Flights.getCodi')
    def test_1_10(self, mock_codi):
        res = Reserva()
        """hacer mock para que el vuelo a españa tenga codigo 1"""
        res.add_destination('Españita')
        """hacer mock para que el vuelo a roma tenga codigo 1"""
        res.add_destination('Roma')
        res.del_destination('Españita')
        mock_codi.return_value = [1]
        self.assertEqual(res.getCodi(), [1])
        
    @mock.patch('src.Flights.Flights.getTotalPrice')
    def test_1_11(self, mock_preu):
        res = Reserva()
        """hacer mock para que el vuelo a españa tenga precio 3"""
        res.add_destination('Españita')
        """hacer mock para que el vuelo a roma  tenga precio 2"""
        res.add_destination('Roma')
        res.del_destination('Españita')
        res.add_Passanger(2)
        mock_preu.return_value = 4
        self.assertEqual(res.getTotalPrice(), 4)
        
    
if __name__ == '__main__':
    unittest.main(exit=False)