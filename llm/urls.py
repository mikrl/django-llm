"""
    The urls.py module contains URL patterns for the LLM app.

    These patterns include:

        queries/ : path mapping to the OpenAIChatQueryListView class
        prompts/ : path mapping to the PromptListView class

    Other URL patterns can also be added here.

"""
from django.urls import path
from llm.views import PromptListView, OpenAIChatQueryListView

urlpatterns = [
    path(
        "queries/",
        OpenAIChatQueryListView.as_view(),
        name="openai_chat_query_list",
    ),
    path("prompts/", PromptListView.as_view(), name="prompt_list"),
    # other URL patterns here...
]
