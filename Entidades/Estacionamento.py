import types

from Entidades.Veiculo import Veiculo


class Estacionamento:
    def __init__(self):
        self.vagasCarrosGrande = [None] * 25
        self.vagasMoto = [None] * 25
        self.vagasCarrosComum = [None] * 50
        self.vagasCarrosGrandeIndisponiveis = 0
        self.vagasMotoIndisponiveis = 0
        self.vagasCarrosComumIndisponiveis = 0

    def adicionarVeiculoVaga(self, veiculo):
        if veiculo.tipoVeiculo == "GRANDE":
            for i in range(len(self.vagasCarrosGrande)):
                if self.vagasCarrosGrande[i] is None:
                    veiculo.numeroVaga = "G" + str(i + 1)
                    self.vagasCarrosGrande[i] = veiculo
                    return print("Carro grande adicionado com sucesso! Seu número de vaga é " + str(veiculo.numeroVaga))
            self.vagasCarrosGrandeIndisponiveis += 1
            return print("Estacionamento Lotado")

        if veiculo.tipoVeiculo == "COMUM":
            for i in range(len(self.vagasCarrosComum)):
                if self.vagasCarrosComum[i] is None:
                    veiculo.numeroVaga = "C" + str(i + 1)
                    self.vagasCarrosComum[i] = veiculo
                    return print("Carro comum adicionado com sucesso! Seu número de vaga é " + str(veiculo.numeroVaga))
            self.vagasCarrosComumIndisponiveis += 1
            return print("Estacionamento Lotado")

        if veiculo.tipoVeiculo == "MOTO":
            for i in range(len(self.vagasMoto)):
                if self.vagasMoto[i] is None:
                    veiculo.numeroVaga = "M" + str(i + 1)
                    self.vagasMoto[i] = veiculo
                    return print("Moto adicionada a vaga com sucesso! Seu número de vaga é " + str(veiculo.numeroVaga))
            self.vagasMotoIndisponiveis += 1
            return print("Estacionamento Lotado")

    def vagasLivres(self):
        countVagasCarrosGrande = 0
        countVagasCarrosComum = 0
        countvagasMoto = 0

        for vaga in self.vagasCarrosGrande:
            if vaga is None:
                countVagasCarrosGrande += 1

        for vaga in self.vagasCarrosComum:
            if vaga is None:
                countVagasCarrosComum += 1

        for vaga in self.vagasMoto:
            if vaga is None:
                countvagasMoto += 1

        return print("VAGAS LIVRES: CARROS COMUNS = " + str(countVagasCarrosComum) + " CARROS GRANDE = " + str(countVagasCarrosGrande) + \
               " MOTOS = " + str(countvagasMoto))

    def removerVeiculoVaga(self,numeroVaga):
        if numeroVaga[0] == 'M':
            for i in range(len(self.vagasMoto)):
                if self.vagasMoto[i] is not None:
                    if self.vagasMoto[i].numeroVaga == numeroVaga:
                         self.vagasMoto[i] = None
                         return print("Vaga removida com sucesso! ")

        if numeroVaga[0] == 'G':
            for i in range(len(self.vagasCarrosGrande)):
                if self.vagasCarrosGrande[i] is not None:
                    if self.vagasCarrosGrande[i].numeroVaga == numeroVaga:
                         self.vagasCarrosGrande[i] = None
                         return print("Vaga removida com sucesso! ")


        if numeroVaga[0] == 'C':
            for i in range(len(self.vagasCarrosComum)):
                if self.vagasCarrosComum[i] is not None:
                    if self.vagasCarrosComum[i].numeroVaga == numeroVaga:
                         self.vagasCarrosComum[i] = None
                         return print("Vaga removida com sucesso! ")

        return print("Número da vaga não é válido! Contate o responsável pelo estabelecimento!")

    def imprimirRelatorio(self):
        return print("CLIENTES NAO ATENDIDOS: CARROS COMUNS = " + str(self.vagasCarrosComumIndisponiveis) + " CARROS GRANDE = " + str(
            self.vagasCarrosGrandeIndisponiveis) + \
                     " MOTOS = " + str(self.vagasMotoIndisponiveis))


if __name__ == '__main__':
    e = Estacionamento()
    e.vagasLivres()
    e.adicionarVeiculoVaga(Veiculo("MOTO"))
    e.adicionarVeiculoVaga(Veiculo("MOTO"))
    e.adicionarVeiculoVaga(Veiculo("MOTO"))
    e.vagasLivres()
    e.removerVeiculoVaga("M2")
    e.vagasLivres()
    e.adicionarVeiculoVaga(Veiculo("MOTO"))
    e.vagasLivres()
    e.imprimirRelatorio()
