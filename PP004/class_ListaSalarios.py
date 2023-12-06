import class_AnaliseDados as AnaliseDados

class ListaSalarios(AnaliseDados.AnaliseDados):
    
    def __init__(self):
        super().__init__(type(float))
        self.__lista = []

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            num_elementos = int(input("Digite o número de elementos na lista de salários: "))
            for _ in range(num_elementos):
                salario = float(input("Digite um salário: "))
                self.__lista.append(salario)
        except ValueError:
            print("Por favor, digite números válidos.")

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
    
    def reajustar_salario(self, salario):
        return salario * 1.1

    def salarios_reajustados(self):
        return list(map(self.reajustar_salario, self.__lista))
    
    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        '''
        Este método retorna uma representação em string da lista de salários
        '''
        sorted_lista = sorted(self.__lista)
        return ', '.join(str(salario) for salario in self.__lista)

    def __init__(self):
        self.__lista = []

    def entradaDeDados(self, salario): 
        self.__lista.append(salario)

    def __str__(self):
        return ', '.join(str(salario) for salario in self.__lista)

    def calcularReajuste(self, percentual):
        for i in range(len(self.__lista)):
            self.__lista[i] *= 1 + percentual / 100
        
        return self.__lista
