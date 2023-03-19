import os
import random
import json
import requests


url = 'https://random-word-api.herokuapp.com/word'
response = requests.get(url)
palavra = json.loads(response.text)
palavra_secreta = palavra[0]

letras_acertadas = ''
contador_de_tentativas = 0
tamanho_palavra_secreta = len(palavra_secreta)
quebra_while = True
tentativas = 0
letras_incorretas = ''
limite_tentativas = len(palavra_secreta) + len(palavra_secreta)

while True:
    print(f'Seu limite de tentativas é {limite_tentativas}')
    letra_digitada = input("Insira uma letra: ")

    if len(letra_digitada) > 1:
        print('Você inseriu mais de uma letra')
        continue
    elif len(letra_digitada) < 1:
        print('Você não inseriu nenhuma letra')
        continue

    tentativas += 1

    palavra_formada = ''
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada 
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra 
        else: 
            palavra_formada += '*'
    if tentativas > limite_tentativas:
        os.system('cls')
        print(f'Você atingiu o número máximo de tentativas.')
        print(f'Você perdeu!\nA palavra secreta era: {palavra_secreta}')
        exit()
    os.system('cls')
    print(f'Letras acertadas: {palavra_formada}\nTentativas: {tentativas}')
    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, você ganhou\n A palavra secreta era: {palavra_secreta}')
        print(f'Você acertou com {tentativas} tentativas')
        exit()



