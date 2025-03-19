class SingleEvent:
    def __init__(self, title="", description="", image=None, choices=None, consequences=None):
        self.title = title
        self.description = description
        self.image = image
        self.choices = choices if choices is not None else []
        self.consequences = consequences if consequences is not None else {} # Example: {'Choice 1': {'attribute': 'vitality', 'value': 10}, 'Choice 2': {'attribute': 'psych', 'value': -5}}

    def apply_consequences(self, choice):
        return self.consequences.get(choice, {})

# TESTS

test_event = SingleEvent(
                         'Test Event',
                         'This is a test event',
                         None,
                         ['Choice 1', 'Choice 2'],
                         {'Choice 1': {'attribute': 'vitality', 'value': 10}, 'Choice 2': {'attribute': 'psych', 'value': -5}}
                         )

print(test_event.apply_consequences('Choice 1')) # Output: {'attribute': 'vitality', 'value': 10}
print(test_event.apply_consequences('Choice 2')) # Output: {'attribute': 'psych', 'value': -5}