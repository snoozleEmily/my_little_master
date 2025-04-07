# Ótima idéia, Little Mistress!

class WrongChapterPhase(Exception):
    def __init__(self, message="Event's and Chapter's phases don't match."):
        super().__init__(message)