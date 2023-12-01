def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado["salario"] *= 1.10

def ler_dados_arquivo(caminho_arquivo):
    empregados = []
    try:
        with open(caminho_arquivo, "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                empregado = {
                    "nome": dados[0],
                    "sobrenome": dados[1],
                    "ano_nascimento": int(dados[2]),
                    "rg": dados[3],
                    "ano_admissao": int(dados[4]),
                    "salario": float(dados[5])
                }
                empregados.append(empregado)
    except FileNotFoundError:
        print(f"O Arquivo não foi encontrado.")
    return empregados