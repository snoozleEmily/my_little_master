import pygame
import random
import string
import numpy as np

# Temos 26 letras no alfabeto (inglês), certo?!
# Se arredondarmos para 25, vamos ter uma conta perfeita!

# 1. Atributos:  Teremos 5 atributos no total.

# 2. Preparação do Alfabeto:  Vamos excluir uma letra aleatória. Assim, ficamos com 25 letras.

# 3. Divisão em Grupos:  As 25 letras resultantes são divididas aleatoriamente em 5 grupos de 5 letras cada.

# 4. Atribuição de Valores às Letras:  Cada letra deve ter um valor atribuído, que é um número aleatório de 1 a 10.
# Se em algum grupo alguma das 5 letras ainda não tiver um valor, será randomizado um valor de 1 a 10 para essa letra,
# repetindo o processo até que todas as letras tenham um valor.
# Observação: Caso uma letra apareça mais de uma vez no nome (input do usuário), o valor dessa letra é considerado apenas uma vez.

# 5. Cálculo dos Pontos por Grupo:  Para cada grupo, soma-se os valores das letras que aparecem no nome do usuário.

# 6. Multiplicação e Limite de Pontuação:  A soma obtida para cada grupo é multiplicada por 2.  O resultado final para cada atributo não pode ultrapassar 100 pontos.

# Ex:  grupo_1 =[A, G, O, J, R]   Random: A=3, G=9, O=1, J=5, R=10  Soma A+G+O+J+R = 27  Multiplica resultado_soma * 2 = 54

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

# 2. Preparação do Alfabeto:  Vamos excluir uma letra aleatória. Assim, ficamos com 25 letras.
def gen_alphabet_values():
    """Gera um dicionário com valores aleatórios para cada letra do alfabeto."""
    letters = list(string.ascii_lowercase)  # Alfabeto em minúsculas
    letters.remove(random.choice(letters))
    values = np.random.randint(1, 10, size=len(letters))
    return dict(zip(letters, values))

# 3. Divisão em Grupos:  As 25 letras resultantes são divididas aleatoriamente em 5 grupos de 5 letras cada.


letters = list(string.ascii_lowercase)  # Alfabeto em minúsculas
print(letters)
letters.remove(random.choice(letters))
values = np.random.randint(1, 10, size=len(letters))
print(letters)
print(values)
dict_test = dict(zip(letters, values))
print(dict_test)