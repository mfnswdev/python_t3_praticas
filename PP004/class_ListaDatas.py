import class_AnaliseDados as AnaliseDados
import class_Data as Data
from class_Data import Data


class ListaDatas(AnaliseDados.AnaliseDados):
    
    def __init__(self):
        super().__init__(type("Data"))
        self.__lista = []

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        while True:
            try:
                num_elementos = int(input("Digite o número de elementos na lista de datas: "))
                for _ in range(num_elementos):
                    while True:
                        try:
                            dia = int(input("Digite o dia: "))
                            mes = int(input("Digite o mês: "))
                            ano = int(input("Digite o ano: "))
                            data = Data.Data(dia, mes, ano)  # Cria um objeto da sua classe Data
                            self.__lista.append(data)
                            break  # Sai do loop interno se a data for válida
                        except ValueError:
                            print("Por favor, digite uma data válida.")
                    print("Data adicionada com sucesso!")
                break  # Sai do loop externo se todas as datas forem adicionadas corretamente
            except ValueError:
                print("Por favor, digite um número válido para o número de elementos.")
            
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
    
    def listarEmOrdem(self):
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        date_strings = [str(date) for date in sorted_lista]
        return date_strings

    def modificar_dia_primeiro(self, data):
        data.dia = 1
        return data

    def datas_anteriores_2019(self):
        return filter(lambda data: data.ano < 2019, self.__lista)

    def datas_modificadas(self):
        return list(map(self.modificar_dia_primeiro, self.datas_anteriores_2019()))
    
    def __iter__(self):
        return iter(self.__lista)

    def __str__(self):
        '''
        Este método retorna uma representação em string da lista de datas
        '''
        sorted_lista = sorted(self.__lista, key=lambda x: (x.ano, x.mes, x.dia))
        return ', '.join(str(data) for data in self.__lista)
    
    def entradaDeDados(self, dia, mes, ano):  
        data = Data(dia, mes, ano)
        self.__lista.append(data)

    def entradaDeDados(self, nova_data):  # Atualizado para receber um objeto Data
        self.__lista.append(nova_data)

    def modificarDatasAnteriores2019(self):
        for i in range(len(self.__lista)):
            if self.__lista[i].ano < 2019:
                self.__lista[i].dia = 1
        
        return self.__lista
