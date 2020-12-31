import time
import random
from setings import logo, giraDado, logoFinal, mostraPontuacao

meta = 0
jogador = []
activate = True
logo()
print("\n\t\t\t\t\t\t\tSeja bem vindo ao jogo DADOS MÁGICOOOSS!!!")
acao1 = input("\nDeseja jogar?")
while activate:
    if acao1.title() == "Não" or acao1.title() == "Nao" or acao1.title() == "N":
        print("\nObrigado pela visita. Até breve...")
        activate = False

    elif acao1.title() == "Sim" or acao1.title() == "S":
        print("\nO jogo funciona da seguite forma:\n"
              "Os jogadores vão girar o dado várias vezes até alcançarem a meta.\n"
              "O primeiro a alcançar a meta, vence o jogo.!\n")

        try:
            meta = int(input("Digite a meta que vocês querem alcançar: "))

            acao2 = int(input("\nTens a possibilidade de jogar com 2, 3 ou 4 jogadores\n"
                              "Deseja jogar com quantos jogadores? \n"))

            if acao2 > 4:
                print("\nO máximo número de jogadores é 4")

            elif acao2 == 2:
                usuario1 = {"nome": input("Digite o nome de um jogador: "), "pontos": 0}
                usuario2 = {"nome": input("Digite o nome de um jogador: "), "pontos": 0}
                jogador = [usuario1, usuario2]
                escolha = random.choice(jogador)
                if escolha == usuario1:
                    print("\nO primeiro a jogar é:")
                    time.sleep(2)
                    print(escolha["nome"])
                    while usuario1["pontos"] < meta or usuario2["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)

                elif escolha == usuario2:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario2["nome"]))
                    while usuario2["pontos"] < meta or usuario1["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)

            elif acao2 == 3:
                usuario1 = {"nome": input("Digite o nome de um jogador: "), "pontos": 0}
                usuario2 = {"nome": input("Digite o nome de outro jogador: "), "pontos": 0}
                usuario3 = {"nome": input("Digite o nome de mais um jogador: "), "pontos": 0}
                jogador = [usuario1, usuario2, usuario3]
                escolha = random.choice(jogador)
                if escolha == usuario1:
                    print("\nO primeiro a jogar é:")
                    time.sleep(2)
                    print(escolha["nome"])
                    while usuario1["pontos"] < meta or usuario2["pontos"] < meta or usuario3["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)

                elif escolha == usuario2:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario2["nome"]))
                    while usuario2["pontos"] < meta or usuario1["pontos"] < meta or usuario3["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)

                elif escolha == usuario3:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario3["nome"]))
                    while usuario3["pontos"] < meta or usuario1["pontos"] < meta or usuario2["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)

            elif acao2 == 4:
                usuario1 = {"nome": input("Digite o nome de um jogador: "), "pontos": 0}
                usuario2 = {"nome": input("Digite o nome de outro jogador: "), "pontos": 0}
                usuario3 = {"nome": input("Digite o nome de mais um jogador: "), "pontos": 0}
                usuario4 = {"nome": input("Digite o nome do último jogador: "), "pontos": 0}
                jogador = [usuario1, usuario2, usuario3, usuario4]
                escolha = random.choice(jogador)
                if escolha == usuario1:
                    print("\nO primeiro a jogar é:")
                    time.sleep(2)
                    print(escolha["nome"])
                    while usuario1["pontos"] < meta or usuario2["pontos"] < meta or usuario3["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada4 = input("\naperte enter para girar o dado " + str(usuario4["nome"]))
                        giraDado(usuario4, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)
                        mostraPontuacao(usuario4)

                elif escolha == usuario2:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario2["nome"]))
                    while usuario2["pontos"] < meta or usuario1["pontos"] < meta or usuario3["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada4 = input("\naperte enter para girar o dado " + str(usuario4["nome"]))
                        giraDado(usuario4, meta)
                        giraDado(usuario4, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)
                        mostraPontuacao(usuario4)

                elif escolha == usuario3:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario3["nome"]))
                    while usuario3["pontos"] < meta or usuario1["pontos"] < meta or usuario2["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada4 = input("\naperte enter para girar o dado " + str(usuario4["nome"]))
                        giraDado(usuario4, meta)
                        giraDado(usuario4, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)
                        mostraPontuacao(usuario4)

                elif escolha == usuario4:
                    print("\nO primeiro a jogar é: ")
                    time.sleep(2)
                    print("\n"+str(usuario4["nome"]))
                    while usuario3["pontos"] < meta or usuario1["pontos"] < meta or usuario2["pontos"] < meta:
                        jogar = input("\naperte enter para girar o dado " + str(usuario4["nome"]))
                        giraDado(usuario4, meta)
                        outrajogada = input("\naperte enter para girar o dado " + str(usuario3["nome"]))
                        giraDado(usuario3, meta)
                        outrajogada3 = input("\naperte enter para girar o dado " + str(usuario2["nome"]))
                        giraDado(usuario2, meta)
                        outrajogada4 = input("\naperte enter para girar o dado " + str(usuario1["nome"]))
                        giraDado(usuario1, meta)
                        giraDado(usuario4, meta)
                        mostraPontuacao(usuario1)
                        mostraPontuacao(usuario2)
                        mostraPontuacao(usuario3)
                        mostraPontuacao(usuario4)
                else:
                    print("Escolha errada!")

            else:
                print("Você não pode jogar sozinho.!\nBrevemente poderás "
                      "jogar contra o computador")

        except ValueError:
            print("\nDigite um número inteiro\n")

    else:
        print("Responda simplesmente (SIM OU NÃO)")
        activate = False

logoFinal()
