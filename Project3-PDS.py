#Equipe: Beatriz Moura, Lucas Lima, Luiz Gadelha

import math #biblioteca utilizada para algumas funções de constantes da math
#bibliotecas abaixo utilizadas para plotagem dos polos e zeros da resultante da transformada Z
import matplotlib.pyplot as plt
from numpy import *
from pylab import *



def option1():#função que roda a opção 1 a qual recebe a equação do sinal analógico
    print("Insira o sinal Analógico\n Exemplos do formato de entrada(sin(x)+cos(x), cos(2*x), 3*tan(2*x)), exp(x) e log(x)")
    x = linspace(-2*pi, 2*pi, 50)
    signal = eval(input())
   
    
    signal1 = []
    x1 = []
    for i in range(0,len(x),2):
      x1.append(x[i])
      signal1.append(signal[i])
      
    sample = x
    sample1 = x1
    
    
    #Plot Analógico
    plt.subplot(2,2,1)
    
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    xticks([]), yticks([])
    plt.title("Sinal Analógico")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    plt.plot(sample,signal,'-')
    


    #plot quantizado
    plt.subplot(2,2,2)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    xticks([]), yticks([])
    plt.title("Sinal Quantizado")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    xi = np.round(3 * signal)
    xQ = 1/3 * xi
    plt.plot(sample,xQ,'-')
    
    
    #plot discretizado
    plt.subplot(2,2,3)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    xticks([]), yticks([])
    plt.title("Sinal Discretizado")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    for i in range(0,len(sample1)):
      plt.stem(sample1,signal1)  
      plt.plot(sample1[i],signal1[i],'o')
    

    
    #plot discretizado quantizado
    plt.subplot(2,2,4)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    xticks([]), yticks([])
    plt.title("Sinal Discretizado Quantizado")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    xj = np.round(signal1)
    xR = 1/3 * xj
    for i in range(0,len(sample1)):
      plt.stem(sample1,xR)  
      plt.plot(sample1[i],xR[i],'o')
    
    
    #mostrando todos os 4 plot
    plt.show()
    #limpando a cada iteração do programa
    plt.clf()
    # OBS.: por estarem no mesmo subplot precisam estar na mesma subrotina
    
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

