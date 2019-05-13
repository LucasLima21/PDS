"""
Equipe 7: Lucas Correia, Lucas Lima, Luiz Gadelha

"""

#bibliotecas utilizadas para construção deste programa
import math #algumas operações e constantes utilizadas

#bibliotcas abaixo para plotagem dos graficos
import matplotlib.pyplot as plt
from pylab import *

def createFunction(entrance): #função que recebe a lista de entrada em string e convert para int e float com eval
    coefSignal = []
    for i in range(len(entrance)):
        coefSignal.append(eval(entrance[i]))
    return coefSignal

def exponent(entrance): # função que monta a lista de expoentes do polinomio, exemplo p3 = [3,2,1,0]
    exp = []
    for i in range(len(entrance)-1, -1, -1):
        exp.append(i)
    return exp

def sampleListConversion(n): #função que monta as amostras em lista de string depois as converte para int/float
    #depois retorna uma lista das amostras digitadas
    sample = []
    root = str(input("Digite o valor das amostras(ex.: 0 0 1): "))
    auxList = root.split()
    for i in range(len(auxList)):
        sample.append(eval(auxList[i]))
    return sample


def sampleResult(entrance, sample, coefSignal, exp, n):
    #função que calcula o valor de cada amostra no sinal e retorna uma lista
    #que contém a resposta do sinal a cada amostra
    resultSignal = []
    for i in range(n):
        result = 0
        for j in range(len(entrance)):
            result += coefSignal[j]*(sample[i]**exp[j])
        resultSignal.append(result)

    return resultSignal


def plotSampleFunction(sample, sampleResult):
    #função que mostra o sinal discreto que fora obtido com cada valor de amostragem
    plt.axhline(0, color = 'black')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid()
    plt.plot(sample, sampleResult,'o')
    plt.show()

def plotFunction(resultSignal):#função que plota a transformada e a convolução, passando somente a lista de sinal resultante
    plt.axhline(0, color = 'black')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid()
    plt.plot(resultSignal,'o')
    plt.show()


def reverseArray(a3): # função que inverte os elementos de uma lista
    decrease = len(a3)-1
    for i in range(int(len(a3)/2)):
        aux = a3[i]
        a3[i] = a3[decrease]
        a3[decrease] = aux
        decrease-=1

    return a3

def shiftRight(a3): #função que os elementos de uma lista, uma vez para a direita
    for i in range(len(a3)-1):
        aux = a3[-i]
        a3[-i] = a3[-i+1]
        a3[-i+1] = aux
    return a3

def convolution(a2, a3):#função que realiza a convolução
    #utilizando o algoritmo que inverte os coef do sinal discreto,
    #multiplica percorrendo o segundo sinal no primeiro e pondo em uma lista o resultado de cada ponto percorrido
    # de um sinal no outro
    size = len(a2)
    convolutionResult = []
    a3 = reverseArray(a3)

    for i in range(len(a2)-1):
        a2.append(0)
        a2.insert(0,0)
        a3.append(0)
        a3.insert(-1,0)

    result = 0
    saveSize = 2*size-1
    for i in range(saveSize):
        for j in range(len(a3)):
            result += (a2[j]*a3[j])

        convolutionResult.append(result)
        a3 = shiftRight(a3)
        result = 0
    return convolutionResult


def fft(a4):#função que realiza a transformada de fourier para sinais discretos, ou seja a fast fourier transform
    #utilizando a formula no livro, e fazendo um somatorio de parte real e imaginaria
    #em cada termo do sinal discreto, obtendo assim o sinal equivalente a transformada de fourier
    w = e**complex(0,-2*pi/len(a4))
    aux = []
    for i in range(len(a4)):
    	temporary = [w**(i*j) for j in range(len(a4))]
    	aux.append(temporary)
    real_and_imaginary = []
    for i in range(len(a4)):
    	sum = 0j
    	for j in range(len(a4)):
    		sum += aux[i][j] * a4[j]
    	real_and_imaginary.append(sum)

    roundedResult = []
    for i in range(len(a4)):
    	roundedResult.append(round(real_and_imaginary[i].real, 2) + round(real_and_imaginary[i].imag, 2)*1j)

    return roundedResult



def option1():# função que realiza a primeira operação do looping
    # recebe um polinomio que representa o sinal discreto, as amostras e plota esse sinal baseado nas amostragens !
    signalInput1 = str(input("Digite o sinal digital(ex.: 1 2 0 1): "))
    entrance1 = signalInput1.split(" ")
    a1 = createFunction(entrance1)
    b1 = exponent(entrance1)
    n = int(input("Digite a quantidade de amostras: "))
    sample = sampleListConversion(n)
    c1 = sampleResult(entrance1, sample, a1, b1, n)
    print(c1)
    plotSampleFunction(sample,c1)
    print('\n')

def option2():# função que realiza a segunda operação
    #recebe dois sinais discretos, realiza a convolução e plota o sinal resultante da convolução
    signalInput2 = str(input("Digite a primeira equação de diferença(ex.: 0 1 2 3): "))
    entrance2 = signalInput2.split(" ")
    a2 = createFunction(entrance2)

    signalInput3 = str(input("Digite a segunda equação de diferença(ex.: 0 2 1 3): "))
    entrance3 = signalInput3.split(" ")
    a3 = createFunction(entrance3)

    result = convolution(a2,a3)
    print(result)
    plotFunction(result)
    print('\n')

def option3():#função que realiza a terceira operação
    #recebe um sinal discreto, realiza a transformada de fourier, e plota a correspondente de fourier
    signalInput4 = str(input("Digite o sinal digital para obter a FFT(ex.: 1 2 0 1): "))
    entrance4 = signalInput4.split(" ")
    a4 = createFunction(entrance4)
    a4 = fft(a4)
    print(a4)
    plotFunction(a4)
    print('\n')

def startProgram():#função que inicializa o programa, o menu e o looping que o usuário escolhe ou não sair ...
    #fica realizando as operações diversas vezes, quantas quiser !!!
    print("Digite as opções:\n[0] para sair\n[1] Para obter inserir um sinal discreto e as amostragens\n[2] Para obter a convolução\n[3] Para obter a Transformada de Fourier\n")
    option = int(input("Escolha a opção: "))
    while(option != 0):
        if(option == 1):
            """
            1) dado um sinal em tempo discreto, apresentar o gráfico correspondente
            """
            option1()
            option = int(input("Escolha a opção: "))
        elif(option == 2):
            """
            2)Dado dois sinais, fazer a convolução entre elas
            """
            option2()
            option = int(input("Escolha a opção: "))
        elif(option == 3):
            """
            3)Dado um sinal, Calcular a Transformada de Fourier e exiba o grafico correspondente
            """
            option3()
            option = int(input("Escolha a opção: "))


#Inicio, chamada da subrotina que inicializa o programa  !!
startProgram()
