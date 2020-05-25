
import unittest
from src.Main import Reserva
from unittest import mock

class TestSkyscanner(unittest.TestCase):
    
    
    def test_1_13(self):
        res = Reserva()
        res.add_destination('Roma')
        res.add_destination('Paris')
        res.add_destination('Españita')
        res.add_Passanger(4)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        confirmacio = res.confirm_reserve()
        self.assertEqual(confirmacio, True)
        
    @mock.patch('src.Skyscanner.Skyscanner.confirm_reserve')
    def test_2_3(self, mock_reserva):
        res = Reserva()
        res.add_destination('Roma')
        res.add_destination('Paris')
        res.add_destination('Españita')
        res.add_Passanger(4)
        res.Insert_User_Data('12345678A', 'Robert', 'Norman', 'Ross', 123456789, 'BobRoss@hotmail.com', 'Male', 'American', 3)
        mock_reserva.return_value = False
        confirmacio = res.confirm_reserve()
        self.assertEqual(confirmacio, False)
if __name__ == '__main__':
    unittest.main(exit=False)