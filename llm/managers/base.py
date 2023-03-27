from django.db import models


class PromptManager(models.Manager):
    def to_json(self):
        return {
            "id": self.id,
            "prompt": self.template,
            "variables": self.get_input_variables(),
        }
