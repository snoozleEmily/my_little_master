import os
import json
import unittest
from jinja2 import Environment, FileSystemLoader, TemplateNotFound



BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "..", "..", "..", "data", "story_content", "Default JSON")


class TestJinjaTemplates(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        """Set up the Jinja2 environment and define test variables."""
        if not os.path.exists(TEMPLATES_DIR):
            raise FileNotFoundError(f"Templates directory not found: {TEMPLATES_DIR}")

        self.env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        self.context = {
            "custom_text": "Your custom introduction text here",
            "CUSTOM_RISING_ACTION_ACT_ONE": "The unexpected twist unfolds.",
            "CUSTOM_RESOLUTION_ACT_ONE": "The consequences ripple through the story.",
            "CUSTOM_ENDING_ACT_ONE": "The chapter closes with uncertainty.",
        }

    def render_template(self, template_name):
        """Helper function to render a template and validate JSON output."""
        template_path = os.path.join(TEMPLATES_DIR, template_name)
        
        if not os.path.exists(template_path):
            self.fail(f"Template '{template_name}' not found in {TEMPLATES_DIR}")

        try:
            template = self.env.get_template(template_name)
        except TemplateNotFound as e:
            self.fail(f"Template '{template_name}' not found: {e}")

        rendered = template.render(self.context)

        try:
            rendered_json = json.loads(rendered)
        except json.JSONDecodeError as e:
            self.fail(
                f"Rendered content from '{template_name}' is not valid JSON. Error: {e}\nContent:\n{rendered}"
            )

        return rendered_json

    def test_default_story(self):
        """Test the DefaultStory JSON template."""
        rendered_json = self.render_template("DefaultStory.json")
        self.assertIsInstance(rendered_json, dict)

    def test_default_choices(self):
        """Test the DefaultChoices JSON template."""
        rendered_json = self.render_template("DefaultChoices.json")
        self.assertIsInstance(rendered_json, dict)

if __name__ == "__main__":
    unittest.main()
