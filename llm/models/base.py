from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelProviderAPI(models.Model):
    """
    Model to store a provider of a LLM API and the associated API key.
    """

    service = models.CharField(_("API Provider"), max_length=100)
    api_key = models.CharField(_("API Key"), max_length=100)

    class Meta:
        verbose_name = _("LLM Provider API")
        verbose_name_plural = _("LLM Provider APIs")
