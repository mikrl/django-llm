from django.db import models


class PromptManager(models.Manager):
    def create_prompt(self, string):
        prompt = self.create(template=string)
        input_vars = prompt.extract_input_vars()
        prompt.num_input_vars = len(input_vars)
        prompt.input_variables = ";".join(input_vars)
        prompt.save()
        return prompt
