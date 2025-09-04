from typing import Optional    


class SingleEvent:
    """
    March 30th, 2025 - Added attribute "story_phase" to determine at what point in the narrative
    the event object will be called. As argument, uses the options listed in ChapterPhaseOptions class or None.
    Usage: ChapterPhaseOptions.[story phase]
    Ex: If chapter_phase = ChapterPhaseOptions.INTRODUCTION, the event will be part of the INTRODUCTION events pool.

    If chapter_phase = None, the event will not belong to any specific event pool.
    As a result, it can be called during any chapter phase.
    """
    def __init__(
                 self,
                 title:str = "",
                 description:str= "",
                 image:Optional[str]=None,
                 choices:Optional[list]=None,
                 consequences:Optional[dict]=None
    ):
        self.title = title
        self.description = description
        self.image = image
        self.choices = choices if choices is not None else []
        # Example: {'Choice 1': {'attribute': 'vitality', 'value': 10}, 'Choice 2': {'attribute': 'psych', 'value': -5}}
        self.consequences = consequences if consequences is not None else {} 

    def apply_consequences(self, choice):
        return self.consequences.get(choice, {})


# -------------------- TESTS ---------------------
if __name__ == "__main__":
    test_event = SingleEvent(
          'Test Event', 'This is a test event', 
          None, ['Choice 1', 'Choice 2'],
          {'Choice 1': {'attribute': 'vitality', 'value': 10}, 
           'Choice 2': {'attribute': 'psych', 'value': -5}}
          )

    # Output: {'attribute': 'vitality', 'value': 10}
    print(test_event.apply_consequences('Choice 1')) 

    # Output: {'attribute': 'psych', 'value': -5}
    print(test_event.apply_consequences('Choice 2')) 