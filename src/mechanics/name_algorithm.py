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
                seed.append(alphabet_values[char])
            additional_seed_values = np.random.randint(0, 9, size=20 - len(seed))
            for seed_val in additional_seed_values:
                seed.append(seed_val)
    else:
        for char in char_name:
            seed.append(alphabet_values[char])

# Ok agora que já consigo gerar a seed,
# preciso arranjar uma forma de fazer com que a seed afete os atributos

# Teste
diction = gen_alphabet_values()
char_name = str("Nabuco de Cortelha").replace(' ', "")
print(char_name)
seed = []

def main():
    alphabet_values = gen_alphabet_values()
    char_name = get_char_name()
    gen_seed(alphabet_values, char_name)



        # isso não faria com que qto mais letras, maior a pontuação?
        # mas aí é só não depender da quantidade
        # como não depender da quantidade?
        # uma seed!
        # sendo que a cada partida, o valor das letras será diferente
        # portanto, o jogador não vai poder antecipar as seeds ao escolher um mesmo nome
        # a seed é de um tamanho único de 20 caracteres
        # cria-se uma seed = []
        # se o nome for menor que 20, faz while len(seed) < 20,
        # adicionando +1 a cada loop em uma variável de contador para controle do while
        # gerando um número aleatório para o espaço vazio
        # e gravando (append) esse número na lista da seed
        # a cada letra do char_name, vai criando um número aleatório com randint para ela
        # resumindo: a cada caracter, mesmo espaço vazio caso char_name < 20, gera-se um randint para ele
        # e armazena na lista seed

        # agora, como fazer essa ligação entre seed e skill? Aliás, seria skill ou atributo?
        # mas isso não importa, o que importa é a lógica
        # a seed sendo uma lista de números,podemos fazer um random.choice para cada atributo

        # pegar exemplos "Joe" (3) "Theófilo" (8) "Ozymandias Nabucor" (17) para testes


