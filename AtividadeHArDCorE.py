import random
lista = [random.randint(1, 100) for _ in range(5)]

def main():
    def adicionarNumero(lista, addNumero):
        addNumero = adicionarNumero
        return lista.append(addNumero)

    def removerNumero(lista, remNumero):
        if remNumero in lista:
            lista.remove(remNumero)

    def somaLista(lista):
        soma = sum(lista)
        return soma
        
    def mediaLista(lista):
        media = sum(lista)/len(lista)
        return media


    while True:
        print("1= Adicionar um número à lista")
        print("2= Remover o número da lista")
        print("3= exibir lista")
        print("4= Calcular a soma dos números da lista")
        print("5= Calcular a média dos números da lista")
        print("6= Sair")

        try:
            operacao = int(input("Qual operação voce deseja? (1,2,3,4,5,6) "))
            if operacao == 1:
                addNumero = int(input("Qual o numero que você quer adicionar? "))
                adicionarNumero(lista, addNumero)
            elif operacao == 2:
                remNumero = int(input("Qual o numero que você deseja remover? "))
                removerNumero(lista, remNumero)
            elif operacao == 3:
                print(lista)
            elif operacao == 4:
                print(somaLista(lista))
            elif operacao == 5:
                print(mediaLista(lista))
            else:
                operacao == 6
                break
        except ValueError:
            print("Não é um numero inteiro")
        except Exception as e:
            return e
        except ZeroDivisionError:
            print("Não é possível dividir por zero!")

if __name__ == '__main__':
    main()