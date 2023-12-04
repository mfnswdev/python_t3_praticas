import class_AnaliseDados as AnaliseDados
import class_Data as Data

class ListaDatas(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("Data"))
        self.__lista = []

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        try:
            num_elementos = int(input("Digite o número de elementos na lista de datas: "))
            for _ in range(num_elementos):
                dia = int(input("Digite o dia: "))
                mes = int(input("Digite o mês: "))
                ano = int(input("Digite o ano: "))
                data = Data(dia, mes, ano)
                self.__lista.append(data)
        except ValueError:
            print("Por favor, digite números válidos.")

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        meio = len(sorted_lista) // 2
        return sorted_lista[meio] if len(sorted_lista) % 2 != 0 else sorted_lista[meio - 1]

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        return min(self.__lista, default=None)

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        return max(self.__lista, default=None)

    def __str__(self):
        '''
        Este método retorna uma representação em string da lista de datas
        '''
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        return ', '.join(str(data) for data in self.__lista)
