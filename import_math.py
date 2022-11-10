import math
from MaquinaEstados import *

tokens = []
TokenInfo = []

numeros = []
operador = []
especiais = []
resultados = []
nomesVariaveis = []
variaveis = {}
lexemas = []
conta = ""


# def matcher(contas):
#   for s in contas:
#     tokens.clear()
#     while (s != ""):
#       houveMatch = False
#       s = s.strip()
#       carac = s.split(None, 1)[0]
#       for token in TokenInfo:
#         igualdade = carac in token[0]
#         if igualdade:
#           houveMatch = True
#           s = s.replace(carac, "", 1)
#           tokens.append((token[1], carac))
#           lexemas.append(carac)
#           break
#       if not houveMatch:
#         print(f"Linha {conta.index(calculo)+1}: lexemas {[s[0]]} inválidos")
#         raise Exception(f"Linha {conta.index(calculo)+1}: Erro léxico")
#     valido()


def valido(tokens):
  for token in tokens:
    if token[0] == "NUMERO":
      numeros.append(token[1])
    if token[0] == "OPERADORES":
      operador.append(token[1])
    if token[0] == "INICIAL":
      especiais.append(token[1])
    if token[0] == "RESULTADO":
      resultados.append(token[1])
    if token[0] == "VARIAVEL":
      nomesVariaveis.append(token[1])
      if token[1] in variaveis:
        numeros.append(variaveis[token[1]])
        resultados.remove(variaveis[token[1]])
  calcular()


def calcular():
  if (len(operador) == 0):
    resultados.append(numeros[0])
    numeros.pop(0)
    armazenarVar()

  for operacao in operador[::-1]:
    if operacao == "+":
      conta = float(numeros[0]) + float(numeros[1])
      remove(2)
    elif operacao == "-":
      conta = float(numeros[0]) - float(numeros[1])
      remove(2)
    elif operacao == "*":
      conta = float(numeros[0]) * float(numeros[1])
      remove(2)
    elif operacao == "/":
      conta = float(numeros[0]) / float(numeros[1])
      remove(2)
    elif operacao == "exp":
      conta = float(numeros[0])**float(numeros[1])
      remove(2)
    elif operacao == "rot":
      conta = float(numeros[0])**(1 / float(numeros[1]))
      remove(2)
    elif operacao == "sin":
      conta = math.sin(float(math.radians(float(numeros[0]))))
      remove(1)
    elif operacao == "cos":
      conta = math.cos(float(math.radians(float(numeros[0]))))
      remove(1)

    numeros.append(conta)
    resultados.append(conta)

    if "?" in especiais:
        refaz()
    if len(nomesVariaveis) != 0:
      armazenarVar()


def refaz():
  for especial in especiais:
    if especial == "?":
      numeros.append(resultados[-1])


def remove(n):
  for i in range(n):
    numeros.pop(0)
  operador.pop(0)


def armazenarVar():
  for nome in nomesVariaveis:
    if nome not in variaveis.keys():
      variaveis[nome] = resultados[-1]

def inicial(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["?", "(", ")", ";"]:
        novoEstado = "INICIAL"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def numero(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["1","2","3","4","5","6","7","8","9","0","."]:
        novoEstado = "NUMERO"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def operacao(string):
    stringSplitted = string.split(None, 1)[0]
    stringSplitted = stringSplitted.strip()
    if stringSplitted in ["+","-","/","*","sin","cos","rot","exp"]:
        novoEstado = "OPERADORES"
    else:
        novoEstado = "ERRO"
    return (novoEstado, stringSplitted)

def variavel(string):
    if len(string) > 1:
      novoEstado = "VARIAVEL"
    else:
        novoEstado = "ERRO"
    return (novoEstado, string)




def limpa():
  numeros.clear()
  tokens.clear()
  especiais.clear()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    return linhas
  
if __name__ == '__main__':
  #conta = input("digite o calculo: ")
    conta = [['( op ( 1 )', '( 2 op + )']]

    fsm = MaquinaEstados()
    fsm.adicionarEstado("INICIAL", inicial, 1)
    fsm.adicionarEstado("NUMERO", numero, 1)
    fsm.adicionarEstado("OPERADORES", operacao ,1)
    fsm.adicionarEstado("VARIAVEL", variavel, 1)
    fsm.setStart("INICIAL")
    for contas in conta:
      for calculo in contas:
        for caractere in calculo.split():
          caractere = caractere.strip()
          fsm.rodar(caractere)
        print(fsm.tokens)
        valido(fsm.tokens)
        fsm.tokens.clear()
    print("Resultado: ", resultados[-1])
    limpa()