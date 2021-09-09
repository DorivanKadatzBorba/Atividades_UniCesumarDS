from pandas import DataFrame as df
from random import randint

agenda = {}
while True:
    print("Selecione uma Opção: \n",
          "1 - Insira um novo cadastro \n",
          "2 - Mostrar todos os cadastros \n",
          "0 - Encerrar")


    def cadastro(nome, telefone, email):
        cod = randint(0, 1000)
        lista = {"Código": cod,
                 "Nome": nome,
                 "Telefone": telefone,
                 "E-mail": email}
        agenda[cod] = lista


    while True:
        try:
            acao = int(input("Opção: "))
        except ValueError:
            print("Error: Opção Inválida")
            continue
        else:
            break

    acao = int(input("Opção: "))
    quantidade_cadastro = len(agenda.keys())

    if acao == 1:
        if quantidade_cadastro < 5:
            cadastro(
                input("Nome: "),
                input("Telefone: "),
                input("E-mail: "))
        else:
            print("Agenda Lotada!")

    elif acao == 2:
        if quantidade_cadastro == 0:
            print("Agenda Vazia!")
        else:
            frame = df(agenda.values())
            print(frame)

    elif acao == 0:
        exit()
