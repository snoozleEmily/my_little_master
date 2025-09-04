from core.text import Text

def start_story(display):
    content = r"Hey Tak Tak! May Abend aid you moosha moosh settings."
    text = Text(display, content, 50, 50, font_size=48, color=(255, 255, 0))
    return text
