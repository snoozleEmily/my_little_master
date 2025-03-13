from character import MainCharacter


# Salvar aqui as instâncias de personagens que morreram
# Ter módulo para:
# - Mostrar o último personagem no end game
# - Mostrar todos os personagens no graveyard
#   -- Mostrar a história completa de cada um. 
#      [problemas com isso: com tempo o jogo vai ficar muito pesado. 
#      Considerar a implementação de clear cache e 
#      salvar os arquivos de histórico em outro lugar,
#      como um arquivo de texto separado, por exemplo]

class Graveyard(MainCharacter): 
    def __init__(self, char_name, aura, spirit, psych, karma, vitality, end_game):
        super().__init__(char_name, aura, spirit, psych, karma, vitality)
        self.end_game = end_game # Should this be here? Or should we handle it outisde the class?
        self.deceased_characters = []

    def add_deceased_character(self, character):
        """
        Adds a deceased character to the graveyard.

        Args:
            character (MainCharacter): The deceased character to add.
        """
        if not character.is_alive:
            self.deceased_characters.append(character)
        if character.is_alive and not self.end_game: #change the var placing?
            print(f"{character.char_name} has reached the end of the game alive.")
        else:
            print(f"{character.char_name} is still alive and cannot be added to the graveyard.")

    def display_life_history(self, character):
        """
        Displays the life history of a deceased character.

        Args:
            character (MainCharacter): The character whose life history to display.
        """
        if character in self.deceased_characters:
            # For testing, must be changed to write to a file or screen
            print(f"Life History of {character.char_name}:")
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
        """
        choice_dict = {
            "event_title": event.title,
            "event_choice": event.choice,
            "consequence": event.consequence,
        }

        self.life_choices.append(choice_dict)
        self.process_life_choices()

        return self.life_choices
    