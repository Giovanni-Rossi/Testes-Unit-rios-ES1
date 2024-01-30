import unittest
import Moeda

class TestMoney(unittest.TestCase):
    def test_RealToDolar(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [0.2015, 0.4029, 0.6709, 1.0073, 4.0292, 10.0729]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.RealToDolar(entrada[i]), esperado[i])
    def test_RealToEuro(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [0.1859,0.3717, 0.6189, 0.9293, 3.7173, 9.2932]
    
        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.RealToEuro(entrada[i]), esperado[i])
    def test_RealToYen(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [29.7796, 59.5593, 99.1662, 148.8982, 595.5926, 1488.9815]
        
        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.RealToYen(entrada[i]), esperado[i])
    def test_RealToPesoArg(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [166.334, 332.668, 553.8922, 831.67, 3326.68, 8316.6999]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.RealToPesoArg(entrada[i]), esperado[i])
    def test_DolarToReal(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [4.9638, 9.9276, 16.5295, 24.819, 99.276, 248.19]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.DolarToReal(entrada[i]), esperado[i])
    def test_EuroToReal(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [5.3803, 10.7606, 17.9164, 26.9015, 107.606, 269.015]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.EuroToReal(entrada[i]), esperado[i])

    def test_YenToReal(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [0.0336, 0.0672, 0.1118, 0.1679, 0.6716, 1.679]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.YenToReal(entrada[i]), esperado[i])
    def test_PesoArgToReal(self):
        entrada = [1, 2, 3.33, 5, 20, 50]
        esperado = [0.006, 0.012, 0.02, 0.0301, 0.1202, 0.3006]

        for i in range(6):
            self.assertEqual(Moeda.ConversorMoeda.PesoArgToReal(entrada[i]), esperado[i])


if __name__ == '__name__':
    unittest.main()
