import random
import time

def logoFinal():
    print("\n|-----------------------------------------------------|")
    print("|-----------------------------------------------------|")
    print("|                    GAME OVER                        |")
    print("|-----------------------------------------------------|")
    print("|-----------------------------------------------------|")

def logo():
    print("\n\t\t\t\t\t\t|--------------------------------------------------|")
    logoName = " Dados Mágicos "
    print(logoName.center(150))
    print("\t\t\t\t\t\t|--------------------------------------------------|")


def giraDado(dict_user, meta):
    dado = random.randint(1,6)
    dict_user["pontos"] += dado
    print(str(dict_user["nome"])+", Obteve "+str(dado)+" pontos")
    if dict_user["pontos"] >= meta:
        time.sleep(2)
        print(str(dict_user["nome"])+" Alcançou a meta mais rápido e obteve "+str(dict_user["pontos"])+" pontos.")
    if dado == 6:
        print(str(dict_user["nome"])+" vai girar novamente")
        giraDado(dict_user, meta)

        logoFinal()
        breakpoint()

def logowinner():
    logoName = " GAME OVER "
    print(logoName.center(50,("=")))

def mostraPontuacao(dicionario):
    print("---------------------------------------------")
    print(str(dicionario["nome"])+" já tem "+str(dicionario["pontos"])+" pontos")
    print("---------------------------------------------")
