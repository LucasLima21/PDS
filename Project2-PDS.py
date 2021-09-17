"""
Equipe 7: Beatriz Moura, Lucas Lima, Luiz Gadelha
UEA - Universidade do Estado do Amazonas
EST - Escola Superior de Tecnologia
Processamendo Digital de Sinais
E-mail: ldsllm.eng@uea.edu.br
"""

"""
Teste de entrada: numerado = 1 0
denominador = 1 0.25 -0.375
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

def plotUnitCircle(): # função que retorna o plot somente da circunferencia de raio R da RDC.
    t = np.linspace(0,2*np.pi,100)
    x = 1*np.cos(t)
    y = 1*np.sin(t)
    return plot(x,y)

def plotFunction(zero, polo): #função recebe lista de zeros e lista de polos

    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('Imaginário')
    plt.xlabel('Real')
    plt.grid()
    plt.axis('equal')
    plotUnitCircle() # plota a circunferencia unitária  R = 1

    #Plota os zeros com parte real e imaginária
    for i in range(len(zero)):
        plt.plot(zero[i].real,zero[i].imag,'o')

    #plota os polos com parte real e imaginária
    for j in range(len(polo)):
        plt.plot(polo[j].real,polo[j].imag,'x')
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
    plotFunction(num,den)
    # plotCircle()
    # plotFunction(den,"x")
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
