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


# Será que o graveyard poderia ser uma subclasse de MainCharacter?
def char_history(self, event):
        choice_dict = {
            "event_title": event.title,
            "event_choice": event.choice,
            "consequence": event.consequence,
        }

        self.life_choices.append(choice_dict)
        self.process_life_choices()

        return self.life_choices