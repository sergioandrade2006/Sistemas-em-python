#resolução do teorema de pitágoras.

import math

print('bem-vindo(a) ao programa que faz a resolução do teorema de pitágoras!')
print('Cálculos\n 1-para encontrar a hipotenusa;\n 2-para encontrar o cateto adjacente;\n 3-para encontrar o cateto oposto; ')
escolha = int(input('adicione o número correspondente a qual cálculo você deseja realizar:'))


if escolha == 1:
    cateto_adjacente = int(input('insira o valor do cateto adjacente: '))
    cateto_oposto = int(input('insira o valor do cateto oposto: '))
    soma = (cateto_adjacente ** 2) + (cateto_oposto ** 2)
    hipotenusa = math.sqrt(soma) 
    print(f'O valor da hipotenusa é: {hipotenusa:.2f}')

elif escolha == 2:
    hipotenusa = int(input('insira o valor da hipotenusa: '))
    cateto_oposto = int(input('insira o valor do cateto oposto: '))
    hipotenusa_quadrado = hipotenusa ** 2
    catetoOposto_quadrado = cateto_oposto ** 2
    subtracao = hipotenusa_quadrado - catetoOposto_quadrado
    cateto_adjacente = math.sqrt(subtracao)
    print(f'O valor do cateto adjascente é: {cateto_adjacente:.2f}')

elif escolha == 3:
    hipotenusa = int(input('insira o valor da hipotenusa: '))
    cateto_adjascente = int(input('insira o valor do cateto adjascente: ')) 
    hipotenusaQuadrado = hipotenusa ** 2
    quadradoAdjascente = cateto_adjascente ** 2
    subtracao2 = hipotenusaQuadrado - quadradoAdjascente
    cateto_oposto = math.sqrt(subtracao2)
    print(f'O valor do cateto oposto é: {cateto_oposto:.2f}')