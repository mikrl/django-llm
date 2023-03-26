import re

from django.db import models
from django.utils.translation import gettext_lazy as _
from llm.managers.base import PromptManager


class Prompt(models.Model):
    template = models.TextField(_("Prompt Template"))
    input_variables = models.CharField(_("Input Variables"), max_length=4096)
    num_input_vars = models.IntegerField(_("Number of Input Variables"), default=0)
    objects = PromptManager()

    class Meta:
        verbose_name = "Prompt"
        verbose_name_plural = "Prompts"

    def extract_input_vars(self):
        # find all substrings within braces
        matches = re.findall(r"{([^}]*)}", self.template)
        # return list of unique matches
        return list(set(matches))
