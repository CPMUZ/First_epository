print('Esse código funciona somente para experimentos lineares.')
#LIBRARY, CONSTANTS AS LISTS
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as plc
dados=[]
testes=[]
ex= 0
#COLECTING DATA
numero= int(input('Quantos expermimentos deseja realizar ? ' ))
while True:
    for i in range(numero):
        exp= float(input('Insira o número de seu experimento sem unidade: ' ))
        dados.append(exp)
    print(dados)
    pergunta= input('Deseja realizar mais algum experimento ? ' )
    if 'não' in pergunta:
        break
    else:
        numero= int(input('Quantos expermimentos deseja realizar ? ' ))
#EXPERIMENTAL AXÍS
n_exp= numero
for i in range(numero):
    ex= ex+1
    testes.append(ex)
#DATA TREATMENT 
media= np.mean(dados)
desvio= np.std(dados)
varianca= np.var(dados)
mediana= np.median(dados)
histograma= np.histogram(dados, testes)
#MMQ CALCULUS
A = np.vstack([dados, np.ones(len(dados))]).T
m, c = np.linalg.lstsq(A, testes, rcond=None)[0]
print('O coeficiente angular m é {}'.format(A))  
print('O coeficiente linear c é {}'.format(c))
#PLOTING GRAFICS
eixox= input('Digite o que deseja de nome para o eixo x: ' )
eixoy= input('Digite o que deseja de nome para o eixo y: ' )
titulo= input('Digite o titulo desejado para o grafico: ' )
plt.style.use('dark_background')
dados_array = np.array(dados)
plt.scatter(dados_array, testes)
plt.plot(dados_array, m*dados_array + c, 'r', label='Reta de Ajuste')
ay = plt.gca()
ay.yaxis.set_major_locator(plc.MaxNLocator(integer=True))
plt.xlabel(eixox)
plt.ylabel(eixoy)
plt.title(titulo)
plt.show()
