from django.db import models
from llm.models.prompts import Prompt


class OpenAIChatManager(models.Manager):
    def to_json(self):
        return {
            "id": self.id,
            "prompt": self.prompt.to_json(),
            "api_key": self.api_key,
            "memory": self.memory,
        }

    def update(self, instance, new_prompt: Prompt):
        instance.update(new_prompt)
