import random
lista = [random.randint(1, 100) for _ in range(5)]


def adicionarNumero(lista, addNumero):
    add = int(addNumero)
    return lista.append(add)

def removerNumero(lista, remNumero):
    rem = int(remNumero)
    return lista.remove(rem)

def somaLista(lista):
    soma = sum(lista)
    return soma
    
def mediaLista(lista):
    media = sum(lista)/len(lista)
    return media

def main():

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
                add = int(input("Qual o numero que você quer adicionar? "))
                adicionarNumero(lista, add)
            elif operacao == 2:
                rem = int(input("Qual o numero que você deseja remover? "))
                removerNumero(lista, rem)
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
        except ZeroDivisionError:
            return print("Não é possível dividir por zero!")
        except Exception as e:
            return e


if __name__ == '__main__':
    main()