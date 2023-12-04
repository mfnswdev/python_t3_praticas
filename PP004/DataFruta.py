import class_ListaNomes as ListaNomes
import class_ListaDatas as ListaDatas
import class_ListaSalarios as ListaSalarios
import class_ListaIdades as ListaIdades

def main():
    nomes = ListaNomes.ListaNomes()
    datas = ListaDatas.ListaDatas()
    salarios = ListaSalarios.ListaSalarios()
    idades = ListaIdades.ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:   
        lista.entradaDeDados()
        print(lista.mostraMediana())
        print(lista.mostraMenor())
        print(lista.mostraMaior())
        print("___________________")

    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
