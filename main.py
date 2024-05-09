from os import system
from termcolor import colored
import requests


def extrair_numeros(texto: str):
    numeros = "".join(num for num in texto if num.isdigit())
    return numeros

def busca_cnpj(numero_cnpj: str):
    cnpj = extrair_numeros(numero_cnpj)
    resposta = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}")
    return resposta.json()

def busca_cep(numero_cep: str):
    cep = extrair_numeros(numero_cep)
    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    return resposta.json()


while True:
    cnpj = str(input("DIGITE UM CNPJ A SER CONSULTADO: ")).strip()
    numero_cnpj = extrair_numeros(cnpj)
    try:
        dados_cnpj = busca_cnpj(numero_cnpj)
    except:
        system("cls")
        print(colored("CNPJ INVÁLIDO, TENTE NOVAMENTE.", "red"))
    else:
        try:
            dados_cep = busca_cep(extrair_numeros(dados_cnpj["cep"]))
        except:
            system("cls")
            print(colored("OCORREU UM ERRO, TENTE NOVAMENTE.", "red"))
        else:
            if dados_cnpj["status"] != "OK":
                system("cls")
                print(colored("CNPJ INVÁLIDO, TENTE NOVAMENTE.", "red"))
            else:
                system("cls")
                print(colored("BUSCA REALIZADA COM SUCESSO!", "green"))
                print(f'\nRAZÃO SOCIAL: {dados_cnpj["nome"].upper()}')
                if 'fantasia' in dados_cnpj and dados_cnpj["fantasia"] != "":
                    print(f'NOME FANTASIA: {dados_cnpj["fantasia"].upper()}')
                print(f'LOGRADOURO: {dados_cep["logradouro"].upper()}')
                print(f'NÚMERO: {int(dados_cnpj["numero"])}')
                if 'complemento' in dados_cnpj and dados_cnpj['complemento'] != "":
                    print(f'COMPLEMENTO: {dados_cnpj["complemento"].upper()}')
                print(f'BAIRRO: {dados_cep["bairro"].upper()}')
                print(f'LOCALIDADE: {dados_cep["localidade"].upper()}')
                print(f'UF: {dados_cep['uf'].upper()}')
                print(f'CEP: {dados_cep["cep"].upper()}\n')
                break
system("PAUSE")
