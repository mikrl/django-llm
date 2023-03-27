"""
    The urls.py module contains URL patterns for the LLM app.

    These patterns include:

        queries/ : path mapping to the OpenAIChatQueryListView class
        prompts/ : path mapping to the PromptListView class

    Other URL patterns can also be added here.

"""
from django.urls import path
from llm.views import (
    PromptDetailView,
    PromptListView,
)  # , OpenAIChatQueryDetailView, OpenAIChatQueryListView

app_name = "llm"

urlpatterns = [
    path("prompts/<int:pk>/", PromptDetailView.as_view(), name="prompt_detail"),
    path("prompts/", PromptListView.as_view(), name="prompt_list"),
]
