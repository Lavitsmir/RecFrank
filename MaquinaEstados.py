class MaquinaEstados:
    def __init__(self):
        self.classificacoes = {}
        self.estadoInicial = None
        self.estadoFinal = []
        self.tokens = []
    def adicionarEstado(self, nome, arrayClassificacoes, fim=0):
        nome = nome.upper()
        self.classificacoes[nome] = arrayClassificacoes
        if fim:
            self.estadoFinal.append(nome)
    def setStart(self, nome):
        self.estadoInicial = nome.upper()

    def rodar(self, texto):
        try:
            estadoAtual = self.classificacoes[self.estadoInicial]
        except:
            raise "Erro de inicialização, por favor, rode o setStart antes"
        if not self.estadoFinal:
            raise "Não existe estado final"

        for key, value in self.classificacoes.items():
            (novoEstado, texto) = self.classificacoes[key](texto)
            if novoEstado in self.estadoFinal:
                print((novoEstado, texto))
                self.tokens.append((novoEstado, texto))
                break
        print(self.tokens)
        



    


