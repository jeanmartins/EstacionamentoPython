from Entidades.Estacionamento import Estacionamento
from Entidades.Veiculo import Veiculo


class Aplicativo:
    def __init__(self):
        self.app = Estacionamento()

    def menu(self):
        print(" -- ESTACIONAMENTO PYTHON --")
        self.app.vagasLivres()
        print("Escolha uma das opções abaixo:")
        print("1 - Estacionar veículo")
        print("2 - Liberar vaga")
        print("3 -  Imprimir relatório")
        print("4 - Encerrar aplicação")
        opcao_menu = input()
        return int(opcao_menu)

    def iniciarApp(self):
        opt = self.menu()
        while opt < 9:
            if opt == 1:
                print("Qual seu tipo de veículo?")
                print("1 - CARRO GRANDE 2- CARRO COMUM 3- MOTO")
                opcaoveiculo = int(input())
                if opcaoveiculo != 1 and opcaoveiculo != 2 and opcaoveiculo != 3:
                    print("Opção inválida!")
                if opcaoveiculo == 1:
                    self.app.adicionarVeiculoVaga(Veiculo("GRANDE"))

                if opcaoveiculo == 2:
                    self.app.adicionarVeiculoVaga(Veiculo("COMUM"))

                if opcaoveiculo == 3:
                    self.app.adicionarVeiculoVaga(Veiculo("MOTO"))

            elif opt == 2:
                print("Informe o número da vaga a ser liberada: ")
                numeroVaga = input()
                self.app.removerVeiculoVaga(numeroVaga)
            elif opt == 3:
                self.app.imprimirRelatorio()
            elif opt == 4:
                quit()
            else:
                print("Opção inválida")

            opt = self.menu()
