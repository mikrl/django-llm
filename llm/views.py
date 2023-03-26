"""
    Module containing views for the LLM Django app.

    Defines the views that render HTML templates for Prompt and OpenAIChatQuery models.

    Classes:
        - OpenAIChatQueryListView: View for displaying a list of OpenAIChatQuery objects.
        - PromptListView: View for displaying a list of Prompt objects.
"""
from django.views.generic import ListView
from llm.models import Prompt
from llm.models.queries import OpenAIChatQuery


class OpenAIChatQueryListView(ListView):
    """
    A view that displays a list of OpenAIChatQuery objects.

    Attributes:
        model: The model that this view displays a list of.
        template_name: The name of the template to render this view.
    """

    model = OpenAIChatQuery
    template_name = "openai_chat_query_list.html"


class PromptListView(ListView):
    """
    A view that displays a list of Prompt objects.

    Attributes:
        model: The model that this view displays a list of.
        template_name: The name of the template to render this view.
    """

    model = Prompt
    template_name = "prompt_list.html"
