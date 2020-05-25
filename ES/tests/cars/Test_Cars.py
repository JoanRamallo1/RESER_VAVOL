

import unittest
from src.Main import Reserva
from unittest import mock

class TestCars(unittest.TestCase):
    
    
    @mock.patch('src.Cars.Cars.get_price_cars')
    def test_3_1(self, mock_preu):
        res = Reserva()
        res.add_Passanger(2)
        res.add_destination('Roma')
        res.add_car(code = 0)
        mock_preu.return_value = 20
        self.assertEqual(res.get_price_cars(), 20)
        
    @mock.patch('src.Cars.Cars.get_price_cars')
    def test_3_2(self, mock_preu):
        res = Reserva()
        res.add_Passanger(2)
        res.add_destination('Roma')
        res.add_car(code = 0)
        res.add_car(code = 1)
        res.del_car(code = 1)
        mock_preu.return_value = 20
        self.assertEqual(res.get_price_cars(), 20)

if __name__ == '__main__':
    unittest.main(exit=False)