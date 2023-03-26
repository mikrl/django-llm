from django.db import models


class OpenAIChatManager(models.Manager):
    def create_from_prompt(self, prompt, **variables):
        obj = self.model(prompt=prompt)
        obj.do_query(**variables)
        obj.save()
        return obj

    def to_json(self):
        super()
        return {
            "id": super().id,
            "prompt": super().prompt.to_json(),
            "api": super().api.to_json(),
            "query_response": super().query_response,
            "memory": super().memory,
        }
