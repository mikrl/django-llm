import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from llm.managers.base import PromptManager


class Prompt(models.Model):
    template = models.TextField(_("Prompt Template"))
    #objects = PromptManager()

    class Meta:
        verbose_name = "Prompt"
        verbose_name_plural = "Prompts"

    @property
    def variables(self):
        # find all substrings within braces
        matches = re.findall(r"{([^}]*)}", self.template)
        # return list of unique matches
        return list(set(matches))
    
    def to_json(self):
        return {
            "id": self.id,
            "prompt": self.template,
            "variables": self.variables,
        }
