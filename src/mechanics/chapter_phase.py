from enum import Enum


# ChapterPhaseOptions class was created to make sure only 
# the listed options or None can be chosen as argument.
class ChapterPhaseOptions(Enum):
    """
    1. INTRODUCTION 
    2. INTRO_AFTER 
    3. PHASE_RISING_ACT
    4. PHASE_CRISIS 
    5. PHASE_RESOLUTION 
    6. ENDING_BEFORE 
    7. ENDING 
    """
    INTRODUCTION = "introduction"
    INTRO_AFTER = "intro_after"
    RISING_ACTION = "rising_action"
    CRISIS = "crisis"
    RESOLUTION = "resolution"
    ENDING_BEFORE = "ending_before"
    ENDING = "ending"