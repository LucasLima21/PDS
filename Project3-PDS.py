#Equipe: Beatriz Moura, Lucas Lima, Luiz Gadelha

import math #biblioteca utilizada para algumas funções de constantes da math
#bibliotecas abaixo utilizadas para plotagem dos polos e zeros da resultante da transformada Z
import matplotlib.pyplot as plt
from numpy import *
from pylab import *

def plotFunction(sample, discretSignal): #função recebe lista amostras da quantização e as aplicações no sinal analogico
    # de cada amostra, ou seja o sinal discretizado
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    plt.title("Sinal Discretizado com 20 amostras");
    for i in range(len(sample)):
        plt.plot(sample[i].real,discretSignal[i],'o')
    plt.stem(sample,discretSignal)
    plt.show()

def option1():#função que roda a opção 1 a qual recebe a equação do sinal analógico
    print("Insira o sinal Analógico\n Exemplos do formato de entrada(sin(x)+cos(x), cos(2*x), 3*tan(2*x)), exp(x) e log(x)")
    x = linspace(-2*pi, 2*pi, 20)
    analogicSignal = eval(input())
    print("Sinal Digital: ", analogicSignal)
    plotFunction(x,analogicSignal)
    print("\n")


def startProgram():#função que inicia o programa, fica em looping mostrando o pequeno menu feito
    #apenas para fins calcular mais de uma vez,

    print("Digite as opções:\n[0] Para sair\n[1] Para inserir a equação do sinal analógico: ")
    option = int(input("Escolha a opção: "))
    while(option != 0):
        if(option == 1):
            option1()
            option = int(input("Escolha a opção: "))



#Inicio!!! chamada da subrotina que inicializa o programa
startProgram()








