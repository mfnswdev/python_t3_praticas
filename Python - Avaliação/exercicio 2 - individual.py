from abc import ABC, abstractmethod
from datetime import datetime

class Dados:
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def __str__(self):
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and self.__mes == outraData.__mes and self.__ano == outraData.__ano

    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False

    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False

class AnaliseDados(ABC):
    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass

    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

class ListaNomes(AnaliseDados):
    def __init__(self):
        super().__init__()
        self.__lista = []

    def entradaDeDados(self):
        quantidade = int(input("Quantos nomes deseja inserir? "))
        for i in range(quantidade):
            nome = input(f"Informe o nome {i + 1}: ")
            self.__lista.append(nome)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            mediana = self.__lista[tamanho // 2 - 1]
        else:
            mediana = self.__lista[tamanho // 2]
        print(f"A mediana dos nomes é: {mediana}")

    def mostraMenor(self):
        menor_nome = min(self.__lista)
        print(f"O menor nome na lista é: {menor_nome}")

    def mostraMaior(self):
        maior_nome = max(self.__lista)
        print(f"O maior nome na lista é: {maior_nome}")

    def __str__(self):
        return ", ".join(self.__lista)

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista de nomes em ordem:")
        for nome in self.__lista:
            print(nome)

class ListaDatas(AnaliseDados):
    def __init__(self):
        super().__init__()
        self.__lista = []

    def entradaDeDados(self):
        quantidade = int(input("Quantas datas deseja inserir? "))
        for i in range(quantidade):
            dia = int(input(f"Informe o dia para a data {i + 1}: "))
            mes = int(input(f"Informe o mês para a data {i + 1}: "))
            ano = int(input(f"Informe o ano para a data {i + 1}: "))
            data = Dados(dia, mes, ano)
            self.__lista.append(data)

    def mostraMediana(self):
        self.__lista.sort(key=lambda x: (x.ano, x.mes, x.dia))
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            mediana = self.__lista[tamanho // 2 - 1]
        else:
            mediana = self.__lista[tamanho // 2]
        print(f"A mediana das datas é: {mediana}")

    def mostraMenor(self):
        menor_data = min(self.__lista)
        print(f"A menor data na lista é: {menor_data}")

    def mostraMaior(self):
        maior_data = max(self.__lista)
        print(f"A maior data na lista é: {maior_data}")

    def __str__(self):
        return "\n".join(str(data) for data in self.__lista)

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista de datas em ordem:")
        for data in self.__lista:
            print(data)

class ListaSalarios(AnaliseDados):
    def __init__(self):
        super().__init__()
        self.__lista = []

    def entradaDeDados(self):
        quantidade = int(input("Quantos salários deseja inserir? "))
        for i in range(quantidade):
            salario = float(input(f"Informe o salário {i + 1}: "))
            self.__lista.append(salario)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            mediana = (self.__lista[tamanho // 2 - 1] + self.__lista[tamanho // 2]) / 2
        else:
            mediana = self.__lista[tamanho // 2]
        print(f"A mediana dos salários é: {mediana}")

    def mostraMenor(self):
        menor_salario = min(self.__lista)
        print(f"O menor salário na lista é: {menor_salario}")

    def mostraMaior(self):
        maior_salario = max(self.__lista)
        print(f"O maior salário na lista é: {maior_salario}")

    def __str__(self):
        return ", ".join(str(salario) for salario in self.__lista)

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista de salários em ordem:")
        for salario in self.__lista:
            print(salario)

class ListaIdades(AnaliseDados):
    def __init__(self):
        super().__init__()
        self.__lista = []

    def entradaDeDados(self):
        quantidade = int(input("Quantas idades deseja inserir? "))
        for i in range(quantidade):
            idade = int(input(f"Informe a idade {i + 1}: "))
            self.__lista.append(idade)

    def mostraMediana(self):
        self.__lista.sort()
        tamanho = len(self.__lista)
        if tamanho % 2 == 0:
            mediana = (self.__lista[tamanho // 2 - 1] + self.__lista[tamanho // 2]) / 2
        else:
            mediana = self.__lista[tamanho // 2]
        print(f"A mediana das idades é: {mediana}")

    def mostraMenor(self):
        menor_idade = min(self.__lista)
        print(f"A menor idade na lista é: {menor_idade}")

    def mostraMaior(self):
        maior_idade = max(self.__lista)
        print(f"A maior idade na lista é: {maior_idade}")

    def __str__(self):
        return ", ".join(str(idade) for idade in self.__lista)

    def listarEmOrdem(self):
        self.__lista.sort()
        print("Lista de idades em ordem:")
        for idade in self.__lista:
            print(idade)

def main():
    # Testando a classe ListaNomes
    nomes = ListaNomes()
    nomes.entradaDeDados()
    nomes.mostraMediana()
    nomes.mostraMenor()
    nomes.mostraMaior()
    nomes.listarEmOrdem()
    
    print("___________________")

    # Testando a classe ListaSalarios
    salarios = ListaSalarios()
    salarios.entradaDeDados()
    salarios.mostraMediana()
    salarios.mostraMenor()
    salarios.mostraMaior()
    salarios.listarEmOrdem()

    print("___________________")

    # Demonstrando os iteradores
    nomes = ['Alice', 'Bob', 'Carol']
    salarios = [2500, 3000, 3500]

    print("Iterador zip:")
    for nome, salario in zip(nomes, salarios):
        print(f"{nome} - Salário: {salario}")

    print("___________________")

    salarios = [2500, 3000, 3500]

    print("Iterador map:")
    salarios_reajustados = list(map(lambda x: x * 1.1, salarios))
    print("Salários reajustados:")
    print(salarios_reajustados)

    print("___________________")

    datas = [datetime(2018, 6, 15), datetime(2019, 4, 20), datetime(2020, 8, 10)]

    print("Iterador filter:")
    datas_modificadas = list(map(lambda x: x.replace(day=1) if x.year < 2019 else x, datas))
    print("Datas modificadas:")
    for data in datas_modificadas:
        print(data.strftime("%d/%m/%Y"))

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
