#Equipe: Beatriz Moura, Lucas Lima, Luiz Gadelha

import math #biblioteca utilizada para algumas funções de constantes da math
#bibliotecas abaixo utilizadas para plotagem dos polos e zeros da resultante da transformada Z
import matplotlib.pyplot as plt
from numpy import *
from pylab import *

def trade_X_to_Y(signalInput):
  concatenation = ""
  for i in range(len(signalInput)):
    if(signalInput[i] == 'x'):
      concatenation+="y"
    else:
        concatenation+=signalInput[i]
  return concatenation

def option1():#função que roda a opção 1 a qual recebe a equação do sinal analógico
    print("Insira o sinal Analogico\n Exemplos do formato de entrada(sin(x) + cos(x), cos(2*x) - 2*sin(x): ")
    x = np.linspace(-2*pi, 2*pi, 60)
    signalInput = input()
    signalNormalFrequency = eval(signalInput)
    #sinal analogico ja com o valor do periodo de amostragem
    
    
    #seguindo o teorema de amostragem de nyquist
    #para que eu nao tenha aliasing
    #preciso representar a frequencia de amostragem
    #com o dobro da frequencia maxima do sinal !!
    #como eu estabeleci uma período que todo sinal terá, o qual é de 2pi
    #logo é só reduzir esse periodo, assim, duplicanddo a frequencia
    y = np.linspace(-4*pi, 4*pi, 80)
    signalInputTraded = trade_X_to_Y(signalInput)
    signalDoubleFrequency = eval(signalInputTraded)
    
    
    #print(x,"\n")
    #print(signal)
    sample = x
    sample1 = y
    
    
    
    #Plot Analogico
    plt.subplot(2,1,1)
    
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    
    plt.title("Sinal Analogico")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    plt.plot(sample,signalNormalFrequency,'-', color='green')
    


    
    #plot discretizado
    plt.subplot(2,1,2)
    plt.subplots_adjust(hspace=0.6, wspace=0.6)
    
    plt.title("Sinal Discretizado")
    plt.axhline(0, color = 'black')
    plt.axvline(0, color = 'black')
    plt.ylabel('X[n]')
    plt.xlabel('n')
    plt.grid()
    #reduzindo pela metade o período, duplicando a frequencia!
    plt.stem(sample1/2,signalDoubleFrequency)  
   

    
 
    
    #mostrando todos os 4 plot
    plt.show()
    #limpando a cada iteracao do programa
    plt.clf()
    # OBS.: por estarem no mesmo subplot precisam estar na mesma subrotina
    
    print("\n")


def startProgram():#funçãoo que inicia o programa, fica em looping mostrando o pequeno menu feito
    #apenas para fins calcular mais de uma vez,

    print("Digite as opções:\n[0] Para sair\n[1] Para inserir a equação do sinal analógico: ")
    option = int(input("Escolha a opção: "))
    while(option != 0):
        if(option == 1):
            option1()
            option = int(input("Escolha a opção: "))



#Inicio!!! chamada da subrotina que inicializa o programa
startProgram()

