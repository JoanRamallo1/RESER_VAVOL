import unittest
from src.Main import Reserva
from unittest import mock


class TestHotels(unittest.TestCase):
    
    @mock.patch('src.Hotels.Hotels.get_price_habitacions')
    def test_3_3(self, mock_preu):
        res = Reserva()
        res.add_Passanger(2)
        res.add_destination('Roma')
        res.add_car(code = 0)
        mock_preu.return_value = 20
        self.assertEqual(res.get_price_habitacions(), 20)
        
    @mock.patch('src.Hotels.Hotels.get_price_habitacions')
    def test_3_4(self, mock_preu):
        res = Reserva()
        res.add_Passanger(2)
        res.add_destination('Roma')
        res.add_car(code = 0)
        res.add_car(code = 1)
        res.del_car(code = 1)
        mock_preu.return_value = 20
        self.assertEqual(res.get_price_habitacions(), 20)
    


if __name__ == '__main__':
    unittest.main(exit=False)