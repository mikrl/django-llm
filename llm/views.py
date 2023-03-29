"""
    Module containing views for the LLM Django app.

    Defines the views that render HTML templates for Prompt and OpenAIChatQuery models.

    Classes:
        - OpenAIChatQueryListView: View for displaying a list of OpenAIChatQuery objects.
        - PromptListView: View for displaying a list of Prompt objects.
"""
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    ModelFormMixin,
    ProcessFormView,
    UpdateView,
)
from llm.forms import PromptForm, ModelProviderAPIForm, OpenAIChatQueryForm
from llm.models import ModelProviderAPI, Prompt
from llm.models.queries import OpenAIChatQuery


class CreatePromptView(CreateView):
    model = Prompt
    form_class = PromptForm
    template_name = "create_prompt.html"
    success_url = reverse_lazy("llm:prompt_list")


class DeletePromptView(DeleteView):
    model = Prompt
    success_url = reverse_lazy("llm:prompt_list")


class ProcessPromptView(ProcessFormView):
    form_class = PromptForm
    template_name = "process_prompt.html"
    success_url = reverse_lazy("llm:prompt_list")

    def form_valid(self, form):
        # Do some processing with the form data here
        return super().form_valid(form)


class EditPromptView(UpdateView, ModelFormMixin):
    model = Prompt
    form_class = PromptForm
    template_name = "edit_prompt.html"
    success_url = reverse_lazy("llm:prompt_list")


class ModelProviderAPIDetailView(DetailView):
    model = ModelProviderAPI
    template_name = "api_detail.html"
    context_object_name = "api"


class ModelProviderAPIListView(ListView):
    model = ModelProviderAPI
    template_name = "api_list.html"
    context_object_name = "modelproviderapis"


class CreateModelProviderAPIView(CreateView):
    model = ModelProviderAPI
    form_class = ModelProviderAPIForm
    template_name = "create_api.html"
    success_url = reverse_lazy("api_list")


class DeleteModelProviderAPIView(DeleteView):
    model = ModelProviderAPI
    template_name = "delete_api.html"
    success_url = reverse_lazy("api_list")


class ProcessModelProviderAPIView(ProcessFormView):
    form_class = ModelProviderAPIForm
    template_name = "process_api.html"
    success_url = reverse_lazy("llm:api_list")

    def form_valid(self, form):
        # Do some processing with the form data here
        return super().form_valid(form)


class EditModelProviderAPIView(UpdateView, ModelFormMixin):
    model = ModelProviderAPI
    form_class = ModelProviderAPIForm
    template_name = "edit_api.html"
    success_url = reverse_lazy("llm:api_list")


class OpenAIChatQueryDetailView(DetailView):
    """
    A view that displays the details of a single OpenAIChatQuery object.

    Attributes:
        model: The model that this view displays the details of.
        template_name: The name of the template to render this view.
        context_object_name: The name to use for the object in the template context.
    """

    model = OpenAIChatQuery
    form_class = OpenAIChatQueryForm
    template_name = "query_detail.html"
    context_object_name = "query"


class OpenAIChatQueryListView(ListView):
    """
    A view that displays a list of OpenAIChatQuery objects.

    Attributes:
        model: The model that this view displays a list of.
        template_name: The name of the template to render this view.
    """

    model = OpenAIChatQuery
    template_name = "query_list.html"


class CreateOpenAIChatQueryView(CreateView):
    """
    A view that provides a form for creating a new OpenAIChatQuery object.

    Attributes:
        model: The model that this view creates a new object of.
        template_name: The name of the template to render this view.
        fields: The fields of the model that should be included in the form.
    """

    model = OpenAIChatQuery
    template_name = "query_form.html"
    fields = ["prompt", "api", "memory"]


class EditOpenAIChatQueryView(UpdateView, ModelFormMixin):
    """
    A view that provides a form for editing an existing OpenAIChatQuery object.

    Attributes:
        model: The model that this view edits an existing object of.
        template_name: The name of the template to render this view.
        fields: The fields of the model that should be included in the form.
    """

    model = OpenAIChatQuery
    form_class = OpenAIChatQueryForm
    template_name = "query_form.html"
    fields = ["prompt", "api", "memory"]


class DeleteOpenAIChatQueryView(DeleteView):
    """
    A confirmation page for deleting an existing OpenAIChatQuery object.

    Attributes:
        model: The model that this view deletes an existing object of.
        template_name: The name of the template to render this view.
        success_url: The URL to redirect to after the object is deleted.
    """

    model = OpenAIChatQuery
    template_name = "query_confirm_delete.html"
    success_url = reverse_lazy("query_list")


class PromptDetailView(DetailView):
    """
    A view that displays the details of a single Prompt object.

    Attributes:
        model: The model that this view displays the details of.
        template_name: The name of the template to render this view.
        context_object_name: The name to use for the object in the template context.
    """

    model = Prompt
    template_name = "prompt_detail.html"
    context_object_name = "prompt"


class PromptListView(ListView):
    """
    A view that displays a list of Prompt objects.

    Attributes:
        model: The model that this view displays a list of.
        template_name: The name of the template to render this view.
    """

    model = Prompt
    template_name = "prompt_list.html"
