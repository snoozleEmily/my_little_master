Vamos ir escrevendo aqui as tarefas que precisamos fazer (em pt_BR mesmo):

# To Dos: 

- [X] EMILY E JOÃO - Brainstorming
- [X] Criar base do projeto
- [] JOÃO - Criar classe do character MVP - in progress
- [] JOÃO - Criar arte do Little Master Tak Tak para o MVP
- [] JOÃO - Criar música intro - in progress
- [] Estruturar a lógica de erros
    - [] Criar pastas default err message
- [] EMILY - Implementar jinja2 e estrutura de condições da história
- [] EMILY - Criar algoritmo do nome / alternativa ao quantum letter matrix
- ~[X] JOÃO - name_algorithm~ Emily vai fazer o algoritmo
    - ~[] fazer o get_names funcionar~


# Obervações:

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
