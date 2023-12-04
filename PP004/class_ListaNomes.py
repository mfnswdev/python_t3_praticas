import class_AnaliseDados as AnaliseDados

class ListaNomes(AnaliseDados.AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        try:
            num_elementos = int(input("Digite o número de elementos na lista de nomes: "))
            for _ in range(num_elementos):
                nome = input("Digite um nome: ")
                self.__lista.append(nome)
        except ValueError:
            print("Por favor, digite um número válido.")

    def mostraMediana(self):
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2
        return sorted_lista[meio]

    def mostraMenor(self):
        '''
        Este método retorna o menor elemento da lista, neste caso o primeiro elemento da lista (index = 0)
        '''
        sorted_lista = sorted(self.__lista)
        return min(sorted_lista, default=None)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista, neste caso o último elemento da lista
        '''
        sorted_lista = sorted(self.__lista)
        return max(sorted_lista, default=None)

    def listarEmOrdem(self):
        sorted_lista = sorted(self.__lista)
        return sorted_lista

    def __str__(self):
        return ', '.join(self.__lista)
        
