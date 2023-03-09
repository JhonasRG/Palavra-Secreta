'''
Se trata de jogo para o usuário adivinhar qual
a palavra secreta.
Nós colocamos uma palavra secreta
qualquer damos a possibilidade para
o usuário digitar apenas uma letra.
Quando o usuário digitar uma letra, o algoritmo
vai conferir se a letra digitada está
na palavra secreta.
Se a letra digitada estiver na
palavra secreta; a letra será exibida.
Se a letra digitada não estiver
na palavra secreta, "*" será exibido no lugar das letras que ainda
precisam ser descobertas.
'''

import os

palavra_secreta = 'Xampoula'
letras_acertadas = ''
contador_de_tentativas = 0
tamanho_palavra_secreta = len(palavra_secreta)
quebra_while = True

while quebra_while:

    letra_digitada = input("Insira uma letra: ")

    if len(letra_digitada) > 1:
        print('Você inseriu mais de uma letra')
        continue
    elif len(letra_digitada) < 1:
        print('Você não inseriu nenhuma letra')
        continue

    palavra_formada = ''
    if letra_digitada in palavra_secreta: # se a letra digitada estiver na palavra secreta
        letras_acertadas += letra_digitada # isso armazena as letras corretas digitadas

    for letra in palavra_secreta: # percorre as letras da palavra secreta
        if letra in letras_acertadas: # se as letras da palavra secreta estiverem dentre as letras acertadas
            palavra_formada += letra # a palavra formada vai receber esta letra
        else: 
            palavra_formada += '*' # caso não esteja, a palavra formada receberá *

    print(palavra_formada)   

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns, você ganhou')
        quebra_while = False


