import unittest
from AtividadeHArDCorE import adicionarNumero,somaLista,removerNumero,mediaLista

class TestAtividade(unittest.TestCase):
    def setUp(self):
        self.lista = [10,20,30]

    def test_add(self):
        lista = [10,20,30]
        adicionarNumero(lista,100)
        self.assertIn(100,lista)

    def test_input(self):
        with self.assertRaises(ValueError):
            adicionarNumero(self.lista,'a')
    
    def test_remove_inexistente(self):
        with self.assertRaises(ValueError):
            removerNumero(self.lista, 100)

    def test_remove(self):
        with self.assertRaises(ValueError):
            removerNumero(self.lista, 100)

    def test_remove_input(self):
        with self.assertRaises(ValueError):
            removerNumero(self.lista,'a')

    def test_soma(self):
        soma = sum(self.lista)
        self.assertEqual(somaLista(self.lista),soma)

    def test_media(self):
        media = sum(self.lista)/len(self.lista)
        self.assertEqual(mediaLista(self.lista),media)
    
    def test_media_zero(self):
        lista=[]
        with self.assertRaises(ZeroDivisionError):
            mediaLista(lista)

if __name__ == '__main__':
    unittest.main()