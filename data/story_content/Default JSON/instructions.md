# How should the JSON files be? [WIP]

## For the MVP
For now, we can have two choices per chapter (act), and when we choose to expand the game, we can add more.
The first choice can be small, affecting the character's status and slightly altering the text, but without changing the story itself.
The second choice could significantly impact the course of the story. For example, the text may be completely different depending on what the player chooses, the main character's status will change, and the story will take a different path.


## Structure

### Jinja2 library

>>> Note: The {% include %} statements are standard Jinja2 syntax for including partial templates. For the custom directives like {% CUSTOM_RISING_ACTION_ACT_ONE %}, you would need to define them—perhaps as macros or pass them as variables in the render context.

### Default Text flow

- `introduction`: 
    Default text independent of any choices.

- `intro_after`: 
    Give a hook for the next phase and the first choice with **custom text.**

- `phase_rising_action`: 
    Development and consequence of the first choice with **custom text.**

- `phase_crisis`: 
    Give a crisis that leads to the second choice with **custom text.**     

- `phase_resolution`: 
    Development text and consequence of the second choice with **custom text.**                         

- `ending_before`: 
    Wrap up the and prepare for the end of the chapter with default text.

- `ending`: 
    End the chapter and make the consequence of the choicess clear with **custom text.**
