class SingleEvent:
    def __init__(self, title="", description="", image=None, choices=None, consequences=None):
        self.title = title
        self.description = description
        self.image = image
        self.choices = choices if choices is not None else []
        self.consequences = consequences if consequences is not None else []
        self.choices_consequences = (choices, consequences)

    # eita, esquece esse código
    # def choice(self, choices_list, choice, consequences_list):
    #     for choice_option in choices_list:
    #         if choice == choice_option:
    #             choice_consequence_tuple = consequences_list[]
    #             return choice