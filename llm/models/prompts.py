from django.db import models
from django.utils.translation import gettext_lazy as _

class Prompt(models.Model):
    template = models.TextField(_("Prompt Template"))
    input_variables = models.CharField("", max_length=4096)