"""
This module defines the LlmConfig class, which is an AppConfig for the 'llm' Django app.

Example usage:

    # In your Django project's settings.py file:
    INSTALLED_APPS = [
        # ... other apps ...
        'llm.apps.LlmConfig',  # Add the LlmConfig app config to INSTALLED_APPS
    ]
"""
from django.apps import AppConfig


class LlmConfig(AppConfig):
    """
    This class defines the configuration for the 'llm' Django app.

    Attributes:
    default_auto_field (str): The default auto field to use for the app's models.
    name (str): The name of the app.

    Example usage:

    # In your Django project's settings.py file:
    INSTALLED_APPS = [
        # ... other apps ...
        'llm.apps.LlmConfig',  # Add the LlmConfig app config to INSTALLED_APPS
    ]
    """

    name = "llm"
    verbose_name = "Large Language Models"
    default_auto_field = "django.db.models.AutoField"
