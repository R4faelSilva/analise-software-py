import unittest
from AtividadeHArDCorE import adicionarNumero,addNumero

class TestAtividade(unittest.TestCase):

    def test_add_numero(self):
        self.assertEqual(adicionarNumero(addNumero))

    def removerNumero(lista, remNumero):
        if remNumero in lista:
            lista.remove(remNumero)

    def somaLista(lista):
        soma = sum(lista)
        return soma
        
    def mediaLista(lista):
        media = sum(lista)/len(lista)
        return media
    
if __name__ == '__main__':
    main()