import os
import json
from jinja2 import Environment, FileSystemLoader

# lmao doesnt work :p

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
STORY_DIR = os.path.join(BASE_DIR, "data", "story_content", "act_one")
TEXT_DIR = os.path.join(BASE_DIR, "data", "Text Database", "act_one")

def load_template(env, template_path):
    try:
        return env.get_template(template_path)
    except Exception as e:
        print(f"Template error: {str(e)}")
        return None

try:
    env = Environment(loader=FileSystemLoader([STORY_DIR, TEXT_DIR]))
    
    json_path = os.path.join(STORY_DIR, "2_after_intro.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    story_template = env.get_template("2_after_intro.jinja2")
    choice_template = env.get_template("choice_one.jinja2")

    print(story_template.render(data))
    print(choice_template.render(data))

except Exception as e:
    print(f"Failed: {str(e)}")