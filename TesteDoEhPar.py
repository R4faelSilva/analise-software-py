import unittest
from TesteDeSoftwareEhPar import eh_par

class TestPar(unittest.TestCase):
    def teste_par(self):
        self.assertTrue(eh_par(6))
    
    def teste_impar(self):
        self.assertFalse(eh_par(3))

if __name__ == '__main__':
    unittest.main()