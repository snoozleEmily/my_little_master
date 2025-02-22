import pygame
import random

# from random import

# 1. Só aceita letras.
# 2. Guardamos o nome inserido.
# 3. Copiamos o valor dessa var em outra
# 4. Colocamos todas as letras em lowercase
# 5. Criamos um alfabeto todo lower case
# 6. No começo de cada novo jogo o algoritmo designa valores aleatórios para cada letra.
#   6.1. Tipo: A letra "y" em uma partida vale 5, mas em uma outra vale "0" e por aí vai...
#        Especificamos que só podem ser usadas letras do alfabeto inglês (já temos um edge case pro algoritmo)


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

    return str(char_name)


def gen_alpha_value(char_name):
    for char in char_name.lower():
        char = random.randint

        # isso não faria com que qto mais letras, maior a pontuação?
        # mas aí é só não depender da quantidade
        # como não depender da quantidade?
        # uma seed!
        # sendo que a cada partida, o valor das letras será diferente
        # portanto, o jogador não vai poder antecipar as seeds ao escolher um mesmo nome
        # a seed é de um tamanho único de 20 caracteres
        # cria-se uma seed = []
        # se o nome for menor que 20, faz while len(char_name) < 20,
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
