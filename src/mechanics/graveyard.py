from character import MainCharacter
import collections


# Salvar aqui as instâncias de personagens que morreram
# Ter módulo para:
# - Mostrar o último personagem no end game
# - Mostrar todos os personagens no graveyard
#   -- Mostrar a história completa de cada um. 
#      [problemas com isso: com tempo o jogo vai ficar muito pesado. 
#      Considerar a implementação de clear cache e 
#      salvar os arquivos de histórico em outro lugar,
#      como um arquivo de texto separado, por exemplo
#
#      uma solução é contabilizar quantos tem no graveyard e passar a deletar os mais antigos após um número limite
#      ex: máximo de 50 chars no graveyard
#      quando vier o 51º, deleta o 1º, já que é o mais antigo]

class Graveyard(MainCharacter): 
    def __init__(self, char_name, aura, spirit, psych, karma, vitality, end_game):
        # Ensure all attributes are ≤ 0
        aura = min(aura, 0)
        spirit = min(spirit, 0)
        psych = min(psych, 0)
        karma = min(karma, 0)
        vitality = min(vitality, 0)

        super().__init__(char_name, aura, spirit, psych, karma, vitality)
        self.end_game = end_game # Should this be here? Or should we handle it outisde the class?
        self.deceased_characters = collections.deque(maxlen=50) # Max 50 chars in the graveyard. Deque automatically deletes the oldest char if limit is reached.
        self.character = {
            "char_name": char_name,
            "aura": aura,
            "spirit": spirit,
            "psych": psych,
            "karma": karma,
            "vitality": vitality,
        }

    def add_deceased_character(self, character):
        """
        Adds a deceased character to the graveyard.

        Args:
            character (MainCharacter): The deceased character to add.
        """
        if not character.is_alive:
            self.deceased_characters.append(character)
            print(f"{self.char_name} has been added to the deceased characters list.")
        elif character.is_alive and not self.end_game: #change the var placing?
            print(f"{self.char_name} has reached the end of the game alive.")
        else:
            print(f"{self.char_name} is still alive and cannot be added to the graveyard.")

    def display_life_history(self, character):
        """
        Displays the life history of a deceased character.

        Args:
            character (MainCharacter): The character whose life history to display.
        """
        if character in self.deceased_characters:
            # For testing, must be changed to write to a file or screen
            print(f"Life History of {self.char_name}:")
            for choice in character.life_choices:
                print(f"Event: {choice['event_title']}")
                print(f"Choice: {choice['event_choice']}")
                print(f"Consequence: {choice['consequence']}")
                print("-" * 20)
        else:
            print(f"{character.char_name} is not in the graveyard.")

    def char_history(self, event):
        """
        Overrides the char_history method from MainCharacter to add Graveyard-specific behavior.
        Uses getattr() with default values to safely access event attributes.
        """
        defaults = {
            # We can change default values later, this is just a placeholder
            'title': 'Unknown Title',
            'choice': 'No Choice Recorded',
            'consequence': 'No Consequence Recorded'
        }
        choice_dict = {
            "event_title": getattr(event, 'title', defaults['title']),
            "event_choice": getattr(event, 'choice', defaults['choice']),
            "consequence": getattr(event, 'consequence', defaults['consequence'])
        }

        self.life_choices.append(choice_dict)
        self.process_life_choices()

        return self.life_choices
    
    def check_graveyard_quantity(self):
        """
        Returns the number of characters in the graveyard.
        """
        return len(self.deceased_characters)


if __name__  == "__main__":
    # ******************* TESTS *******************
    dead_char = MainCharacter("Dead", 1, 2, 1, 4, 5)
    alive_char = MainCharacter("Alive", 2, 3, 2, 5, 10)
    
    # Test clamping attributes
    graveyard = Graveyard(char_name= 'MC',aura=5, spirit=-3, psych=2, karma=-1, vitality=10, end_game=False)

    dead_char.is_alive = False
    
    # Test adding deceased character (game ongoing)
    graveyard.add_deceased_character(dead_char)
    
    # Test adding alive character (game ongoing)
    graveyard.add_deceased_character(alive_char) 
    
    # Test adding alive character (game ended)
    graveyard.add_deceased_character(alive_char)
    
    # Display history
    graveyard.display_life_history(dead_char)
    graveyard.display_life_history(alive_char)  # It should not be called in graveyard?

    # Graveyard quantity
    print(graveyard.check_graveyard_quantity())