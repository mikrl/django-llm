from django import forms
from django.forms import ModelChoiceField
from llm.models import Prompt, ModelProviderAPI
from llm.models.queries import OpenAIChatQuery


class PromptForm(forms.ModelForm):
    template = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    class Meta:
        model = Prompt
        fields = ("template",)


class ModelProviderAPIForm(forms.ModelForm):
    service = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    api_key = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = ModelProviderAPI
        fields = (
            "service",
            "api_key",
        )


class OpenAIChatQueryForm(forms.ModelForm):
    class Meta:
        model = OpenAIChatQuery
        fields = ["prompt", "api", "memory"]

    prompt = ModelChoiceField(
        queryset=Prompt.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Prompt",
    )
    api = ModelChoiceField(
        queryset=ModelProviderAPI.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"}),
        label="API Provider",
    )
    memory = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Memory",
        required=False,
        help_text="Enable memory for this query.",
    )
