# import quantum_letter_matrix as qlm
import os
import event

# Esse log / histórico poderia, por exemplo, gravar o que ele fez no evento X e a consequência daquilo,
# assim fica uma espécie de história da vida dele depois que ele morre,
# com os eventos que ocorreram na vida dele e quais foram suas escolhas.

# E então pode ter uma opção no menu principal que mostra os MCs passados (tipo um Graveyard),
# com suas histórias de vida.

# Isso seria uma espécie de função log da classe main_character que é depois pega pelo jogo
# pra montar o Graveyard e também pode mostrar na tela de game over.



class MainCharacter:
    def __init__(self, char_name, aura, spirit, psych, karma, vitality):
        self.char_name = char_name

        self.attributes = {
            'aura': aura,
            'spirit': spirit,
            'psych': psych,
            'karma': karma,
            'vitality': vitality
        }

        self.life_choices = []

        self.is_alive = True

        self.base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.char_dir = os.path.join(self.base_dir, "data", "characters", char_name)
        self.file_path = os.path.join(self.char_dir, f"{self.char_name}.txt")


        os.makedirs(self.char_dir, exist_ok=True)

        # with open(f"{self.char_dir}\\{char_name}.txt", "w") as char_hist_file:
        if not os.path.exists:
            with open(self.file_path, "w") as char_hist_file:
                char_hist_file.write(f"{char_name}'s Life History\n")

    def check_status(self):  # Checks if all attributes > 0, else it's false and char is dead
        self.is_alive = all(value > 0 for value in self.attributes.values())

        if not self.is_alive:
            with open(self.file_path, "a") as char_hist_file:
                char_hist_file.write(f"\n{self.char_name} has perished.\n")

        return self.is_alive

    def increase_attribute(self, str_attribute, number):
        self.attributes[str_attribute] += number
        self.check_status()

    def decrease_attribute(self, str_attribute, number):
        self.attributes[str_attribute] -= number
        self.check_status()

    def make_choice(self, event, choice, consequence):
        choice = choice

        return choice

    def char_history(self, event):
        choice_dict = {
            'event_title': event.title,
            'event_choice': event.choice,
            'consequence': event.consequence
        }

        self.life_choices.append(choice_dict)

        self.process_life_choices()

        return self.life_choices

    def process_life_choices(self):
        if not self.life_choices:
            return

        last_choice = self.life_choices[-1]

        with open(self.file_path, "a") as char_hist_file:
            char_hist_file.write(f"{last_choice['event_title']}\n"
                                 f"{last_choice['event_choice']}\n"
                                 f"{last_choice['consequence']}\n")


#'''
# ******************* TESTS *******************
# init MainCharacter OK
test_char = MainCharacter("TestChar", 1, 2, 1, 4, 5)

# check_status OK
print(f"check_status: {test_char.check_status()}") # Expected: True Actual: True

# increase_attribute OK
print(f"psych: {test_char.attributes['psych']}") # Expected: 1 Actual: 1
test_char.increase_attribute('psych', 5)
print(f"psych after increase: {test_char.attributes['psych']}") # Expected: 5 Actual: 5

# decrease_attribute OK
print(f"vitality: {test_char.attributes['vitality']}") # Expected: 5 Actual: 5
test_char.decrease_attribute('vitality', 2)
print(f"vitality after decrease: {test_char.attributes['vitality']}") # Expected: 3 Actual: 3

# char_history
choices_list = ['Option A', 'Option B']

consequence_option_a = test_char.decrease_attribute("vitality", 3)
consequence_option_b = test_char.increase_attribute("vitality", 1)
consequences_list = [consequence_option_a, consequence_option_b]

test_event = event.SingleEvent("Test Event",
                               "This is a test event's description",
                               "Image",
                               choices_list[0],
                               consequences_list[0])

test_char.char_history(test_event)
test_char.check_status()





#'''
