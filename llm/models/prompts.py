from django.db import models
from django.utils.translation import gettext_lazy as _


class Prompt(models.Model):
    template = models.TextField(_("Prompt Template"))
    input_variables = models.CharField(_("Input Variables"), max_length=4096)

    class Meta:
        verbose_name = "Prompt"
        verbose_name_plural = "Prompts"
