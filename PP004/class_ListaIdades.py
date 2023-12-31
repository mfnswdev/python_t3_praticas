import class_AnaliseDados as AnaliseDados

class ListaIdades(AnaliseDados.AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            num_elementos = int(input("Digite o número de elementos na lista de idades: "))
            for _ in range(num_elementos):
                idade = int(input("Digite uma idade: "))
                self.__lista.append(idade)
        except ValueError:
            print("Por favor, digite números inteiros válidos.")

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista.
        Se o número de elementos for par, retorna a média entre os dois valores do meio.
        '''
        sorted_lista = sorted(self.__lista)
        meio = len(sorted_lista) // 2

        if len(sorted_lista) % 2 == 0:
            # Se a quantidade de elementos for par, calcula a média entre os dois valores do meio
            return (sorted_lista[meio - 1] + sorted_lista[meio]) / 2
        else:
            # Se a quantidade de elementos for ímpar, retorna o valor exato do meio
            return sorted_lista[meio]

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        sorted_lista = sorted(self.__lista)
        return min(self.__lista, default=None)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        sorted_lista = sorted(self.__lista)
        return max(self.__lista, default=None)

    def listarEmOrdem(self):
        sorted_lista = sorted(self.__lista)
        return sorted_lista

    def __str__(self):
        '''
        Este método retorna uma representação em string da lista de idades
        '''
        sorted_lista = sorted(self.__lista)
        return ', '.join(str(idade) for idade in self.__lista)
    
    def entradaDeDados(self, nova_idade): 
        self.__lista.append(nova_idade)
