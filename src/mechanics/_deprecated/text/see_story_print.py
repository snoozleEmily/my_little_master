import os, json
from jinja2 import Environment, FileSystemLoader


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORY_DIR = os.path.join(BASE_DIR, "..", "..", "..", "data", "story_content", "act_one")  # Change act
FILE_NAME = "1_introduction"  # Change file name

# Debug
print("\n---------------------------------")
print(f"🔍 Checking path: {STORY_DIR}")
print(f"📂 Directory exists? {os.path.exists(STORY_DIR)}\n")

if not os.path.exists(STORY_DIR):
    print("❌ The directory does not exist. Please check the path.\n")
else:
    try:
        # Load JSON file
        json_path = os.path.join(STORY_DIR, FILE_NAME + ".json")
        with open(json_path, "r", encoding="utf-8") as f:
            intros = json.load(f)

        # Set up Jinja2
        env = Environment(loader=FileSystemLoader(STORY_DIR))
        template = env.get_template(FILE_NAME + ".jinja2")

        # Render template with JSON data
        rendered_text = template.render(intros=intros)

        print("✅ Yay! Everything is working fine.\n")
        print("📜 Rendered template output:\n")
        print(rendered_text)
        print("\n---------------------------------")

    except Exception as e:
        print(f"❌ An error occurred: {e}\n")