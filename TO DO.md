Vamos ir escrevendo aqui as tarefas que precisamos fazer (em ptBR mesmo):


# To Dos: 
- [X] EMILY E JOÃO - Brainstorming
- [X] Criar base do projeto
- [] Criar classe do character
- [] Estruturar a lógica de erros
    - [] Criar pastas default err message
- [] EMILY - Implementar jinja2 e estrutura de condições da história
- [] JOÃO - name_algorithm
    - [] fazer o get_names funcionar


# Obervações:

- Classe do character
```python
Attributes of the character (int)
self.constitution = 100
self.psyche = 100
self.fate = 100
self.spirit = 100

States of the character (boolean)
self.normal_character = True

if const <= 0:
self.dead_character = True
self.normal_character = False
Game over

if psi <= 0:
self.insane_character = True
self.normal_character = False
Loses control of actions, loses agency

if spirit <= 0:
self.enslaved_character = True
self.normal_character = False
Loses control of actions, loses agency

if fate <= 0:
self.unlucky_character = True
self.normal_character = False
Higher chances of negative events
```

- Diretrizes - Sistema de valores - alfabeto - nome
Então, a ideia seria:
1. Só aceita letras.
2. Guardamos o nome inserido.
3. Copiamos o valor dessa var em outra
4. Colocamos todas as letras em lowercase
5. Criamos um alfabeto todo lower case
6. No começo de cada novo jogo o algoritmo designa valores aleatórios para cada letra. <br>
6.1. Tipo: A letra "y" em uma partida vale 5, mas em uma outra vale "0" e por aí vai... <br>
Especificamos que só podem ser usadas letras do alfabeto inglês (já temos um edge case pro algoritmo)
