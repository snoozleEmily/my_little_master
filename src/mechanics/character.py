# import quantum_letter_matrix as qlm
import os
import event
import itertools

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
            "aura": aura,
            "spirit": spirit,
            "psych": psych,
            "karma": karma,
            "vitality": vitality,
        }

        self.life_choices = []

        self.is_alive = True

        self.base_dir = os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )


        self.char_dir = os.path.join(self.base_dir, "data", "characters", char_name)

        # Generates a new char_dir if char_dir already exists
        self.char_dir = self.generate_dir_name(self.char_dir)

        os.makedirs(self.char_dir, exist_ok=True)

        self.file_path = os.path.join(self.char_dir, f"{self.char_name}.txt")

        # with open(f"{self.char_dir}\\{char_name}.txt", "w") as char_hist_file:
        if not os.path.exists:
            with open(self.file_path, "w") as char_hist_file:
                char_hist_file.write(f"{char_name}'s Life History\n")

    def generate_dir_name(self, base_dir_path):
        """
        March 15th, 2025 - Added a function to generate a new char_dir if char_dir already exists

        Arg:
            base_dir_path: The self.char_dir path you want to check.

        Returns:
            if char_dir doesn't exist: returns the path set in self.char_dir without changes

            if char_dir already exists: returns the path with modified name using a counter.
                Example: If "TestChar" already exists and you want to create another "TestChar" dir,
                the function will name the new dir as "TestChar(1)".
                If you try to create yet another TestChar dir, this time it will be named "TestChar(2)" and so on...
        """
        if not os.path.exists(base_dir_path):
            return base_dir_path
        else:
            return next(f"{base_dir_path}({i})" for i in itertools.count(1) if not os.path.exists(f"{base_dir_path}({i})"))

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

    def make_choice(self, event, choice_index):
        """
        Handles the character's choice during an event, records the choice and consequence,
        and updates the character's attributes based on the consequence.

        Args:
            event (SingleEvent): The event object containing choices and consequences.
            choice_index (int): The index of the chosen option in the event's choices list.

        Returns:
            str: The chosen option.

        Raises:
            ValueError: If the choice_index is out of bounds for the event's choices list.
        """
        if 0 <= choice_index < len(event.choices):
            choice = event.choices[choice_index]
            consequence = event.consequences[choice_index]

            # Store the event details
            choice_dict = {
                "event_title": event.title,
                "event_choice": choice,
                "consequence": consequence,
            }

            self.life_choices.append(choice_dict)
            self.process_life_choices()

            if isinstance(consequence, dict):
                attribute = consequence.get("attribute") # Attribute to modify (e.g., "vitality")
                value = consequence.get("value") # Value to add/subtract from the attribute
                if value > 0: # Increase
                    self.increase_attribute(attribute, value)
                else: # Decrease
                    self.decrease_attribute(attribute, abs(value))
            return choice
        else:
            raise ValueError("Invalid choice index")

    

    def process_life_choices(self):
        if not self.life_choices:
            return

        last_choice = self.life_choices[-1]

        with open(self.file_path, "a") as char_hist_file:
            char_hist_file.write(
                f"{last_choice['event_title']}\n"
                f"{last_choice['event_choice']}\n"
                f"{last_choice['consequence']}\n"
            )


if __name__  == "__main__":

    # ******************* TESTS *******************
    # init MainCharacter OK
    test_char = MainCharacter("TestChar", 1, 2, 1, 4, 5)

    # check_status OK
    print(f"check_status: {test_char.check_status()}")  # Expected: True Actual: True

    # increase_attribute OK
    print(f"psych: {test_char.attributes['psych']}")  # Expected: 1 Actual: 1
    test_char.increase_attribute("psych", 5)
    print(
        f"psych after increase: {test_char.attributes['psych']}"
    )  # Expected: 5 Actual: 5

    # decrease_attribute OK
    print(f"vitality: {test_char.attributes['vitality']}")  # Expected: 5 Actual: 5
    test_char.decrease_attribute("vitality", 2)
    print(
        f"vitality after decrease: {test_char.attributes['vitality']}"
    )  # Expected: 3 Actual: 3

    choices_list = ["Option A", "Option B"]

    consequences_list = [
        {"attribute": "vitality", "value": -3},
        {"attribute": "vitality", "value": 1},
    ]
    test_event = event.SingleEvent(
        title="Test Event",
        description="This is a test event's description",
        image="Image",
        choices=choices_list,
        consequences=consequences_list,
    )

    # Simulate making a choice (Option A)
    test_char.make_choice(test_event, 0) # 0 = A
    test_char.check_status()
