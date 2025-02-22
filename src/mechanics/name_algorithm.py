import pygame
import random
import string
import numpy as np

# from random import

# 1. Só aceita letras.
# 2. Guardamos o nome inserido.
# 3. Copiamos o valor dessa var em outra
# 4. Colocamos todas as letras em lowercase
# 5. Criamos um alfabeto todo lower case
# 6. No começo de cada novo jogo o algoritmo designa valores aleatórios para cada letra.
#   6.1. Tipo: A letra "y" em uma partida vale 5, mas em uma outra vale "0" e por aí vai...
#        Especificamos que só podem ser usadas letras do alfabeto inglês (já temos um edge case pro algoritmo)

pygame.font.init()
pygame.display.init()

# ainda preciso fazer o get_names funcionar
def get_char_name(screen, font=pygame.font.Font(None, 40)):
    char_name = ""
    active = True

    while active:
        screen.fill((30, 30, 30))

        # Show instructions
        instruction_text = font.render(
            "Type your name (3-20 letters) and press ENTER: ", True, (255, 255, 255)
        )
        screen.blit(instruction_text, (50, 50))

        # Show typed name
        name_text = font.render(char_name, True, (255, 255, 255))
        screen.blit(char_name, (50, 100))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and 3 <= len(char_name) <= 20:
                    active = False
                elif event.key == pygame.K_BACKSPACE:
                    char_name = char_name[:-1]
                else:
                    char = event.unicode
                    if char.isalpha:  # 1. Only accepts letters
                        char_name += char  # 2. Stores inserted name

    return str(char_name.strip().replace(' ', ""))

def gen_alphabet_values():
    """Gera um dicionário com valores aleatórios para cada letra do alfabeto."""
    letters = list(string.ascii_lowercase)  # Alfabeto em minúsculas
    values = np.random.randint(0, 9, size=len(letters))
    return dict(zip(letters, values))

def gen_seed(alphabet_values, char_name):
    seed = []
    char_name = char_name.lower().strip().replace(' ', "")
    if len(char_name) < 20:
        while len(seed) < 20:
            for char in char_name:
                seed.append(alphabet_values[char])  # append os valores atribuídos a cada letra do nome
            additional_seed_values = np.random.randint(0, 9, size=20 - len(seed))
            for seed_val in additional_seed_values:
                seed.append(seed_val)  # para completar o resto, são gerados valores aleatórios e estes, adicionados à seed
    else:  # caso o char_name tenha 20 caracteres, usa-se os valores atribuídos às letras
        for char in char_name:
            seed.append(alphabet_values[char])

    return seed

# Ok agora que já consigo gerar a seed,
# preciso arranjar uma forma de fazer com que a seed afete os atributos

# Essa set_attributes ficou feio demais, depois eu vejo uma forma melhor de fazer essa função
# mas a lógica é essa.
# Os prints são só pra testar mesmo, não vou deixar aqui

# Como a seed define os atributos?
# Minha ideia de uso da seed é simplesmente somar os 5 primeiros números para o primeiro atributo (aura)
# Depois vou somando os outros em ranges de 5 números subsequentes para cada atributo
# É algo bem simples, mas precisaríamos definir o mínimo e o máximo de cada atributo
# pra saber os valores estão muito baixos ou muito altos

# Atualmente o valor mais alto possível para cada atribudo individual é 45, mas é extremamente improvável de acontecer
# (np.randint de 0 a 9, só vai dar 45 se o gerador de seed conseguir a proeza de retornar valor 9 para todas as letras
# do char_name)
def set_attributes(seed, aura_param, spirit_param, psyche_param, fate_param):
    aura_param, spirit_param, psyche_param, fate_param = 0, 0, 0, 0
    for seed_val in seed[:4]:
        aura_param += seed_val
        print(f"aura + seed_val:{aura_param - seed_val} + {seed_val} = {aura_param}")
    for seed_val in seed[5:9]:
        spirit_param += seed_val
        print(f"spirit + seed_val:{spirit_param - seed_val} + {seed_val} = {spirit_param}")
    for seed_val in seed[10:14]:
        psyche_param += seed_val
        print(f"psyche + seed_val:{psyche_param - seed_val} + {seed_val} = {psyche_param}")
    for seed_val in seed[15:19]:
        fate_param += seed_val
        print(f"fate + seed_val:{fate_param - seed_val} + {seed_val} = {fate_param}")
    sum_dict = {
        'aura': aura_param,
        'spirit': spirit_param,
        'psyche': psyche_param,
        'fate': fate_param
    }
    return sum_dict

# Teste
alphabet_values = gen_alphabet_values()
char_name = str("Nabuco de Cortelha").replace(' ', "")
print(char_name)
seed = gen_seed(alphabet_values, char_name)
sum_dict = set_attributes(seed, 'aura', 'spirit', 'psyche', 'fate')
print(sum_dict)

# Não sei se deixo essa main... vou comentar ela, acredito que esse name_algorithm pode ser melhor
# aproveitado sendo importado pelo arquivo que controla a criação de personagem
# def main():
#     alphabet_values = gen_alphabet_values()
#     char_name = get_char_name()
#     seed = gen_seed(alphabet_values, char_name)
#     sum_dict = set_attributes(seed, aura, spirit, psyche, fate)
