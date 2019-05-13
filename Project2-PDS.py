"""
Equipe 7: Beatriz Moura, Lucas Lima, Luiz Gadelha
"""


import math #biblioteca utilizada para algumas funções de constantes da math

#bibliotecas abaixo utilizadas para plotagem dos polos e zeros da resultante da transformada Z
import matplotlib.pyplot as plt
from numpy import *
from pylab import *

def createFunction(entrance): # função que ja recebe a lista de polinimios e os converte para int/float
    coefSignal = []
    for i in range(len(entrance)):
        coefSignal.append(eval(entrance[i]))
    return coefSignal

def plotFunction(resultSignal, symbol): #função que plota o os zeros e os polos conforme com o símbolo que recebe na entrada
    # sendo "o" para os zeros e "x" para os polos
    plt.axhline(0, color = 'black')
    plt.ylabel('Imaginário')
    plt.xlabel('Real')
    plt.grid()
    plt.plot(resultSignal,symbol)
    plt.show()



def findRoots(a):#função que retorna as raizes reais/imaginárias dos polinomios
    aux = roots(a)
    return aux

def rounding(aux):#função que arredonda a saida, para facilitar a visualização das raízes, utilizando função round
    real_and_imaginary = []
    for i in range(len(aux)):
        real_and_imaginary.append(round(aux[i].real, 2) + round(aux[i].imag, 2)*1j)
    return real_and_imaginary

def option1():#função que roda a opção 1 a qual recebe o numerador e denominador da correspondete transformada Z
    numerator = str(input("Digite o numerador: "))
    denominator = str(input("Digite o denominador: "))
    entrance1 = numerator.split(" ")
    entrance2 = denominator.split(" ")
    a1 = createFunction(entrance1)
    a2 = createFunction(entrance2)
    aux1 = findRoots(a1)
    aux2 = findRoots(a2)
    num = rounding(aux1)
    den = rounding(aux2)
    print(num)
    print(den)
    plotFunction(num,"o")
    plotFunction(den,"x")
    print("\n")


def startProgram():#função que inicia o programa, fica em looping mostrando o pequeno menu feito
    #apenas para fins calcular mais de uma vez,
    print("Digite as opções:\n[0] Para sair\n[1] Para obter os zeros e os polos da Transformada-Z ")
    option = int(input("Escolha a opção: "))
    while(option != 0):
        if(option == 1):
            option1()
            option = int(input("Escolha a opção: "))



#Inicio!!! chamada da subrotina que inicializa o programa
startProgram()
