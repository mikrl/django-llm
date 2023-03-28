"""
    The urls.py module contains URL patterns for the LLM app.

    These patterns include:

        queries/ : path mapping to the OpenAIChatQueryListView class
        prompts/ : path mapping to the PromptListView class
        new-prompt/ : path mapping to the prompt_create_view function
        new-provider-api/ : path mapping to the provider_api_create_view function

    Other URL patterns can also be added here.

"""
from django.urls import re_path
from llm.views import (
    PromptDetailView,
    PromptListView,
    CreatePromptView,
    EditPromptView,
    DeletePromptView,
    ModelProviderAPIDetailView,
    ModelProviderAPIListView,
    CreateModelProviderAPIView,
    EditModelProviderAPIView,
    DeleteModelProviderAPIView,
    OpenAIChatQueryDetailView,
    OpenAIChatQueryListView,
    CreateOpenAIChatQueryView,
    EditOpenAIChatQueryView,
    DeleteOpenAIChatQueryView,
)

app_name = "llm"

urlpatterns = [
    re_path(r"^prompt/(?P<pk>\d+)/$", PromptDetailView.as_view(), name="prompt_detail"),
    re_path(r"^prompt/$", PromptListView.as_view(), name="prompt_list"),
    re_path(r"^prompt/create/$", CreatePromptView.as_view(), name="create_prompt"),
    re_path(
        r"^prompt/(?P<pk>\d+)/update/$", EditPromptView.as_view(), name="update_prompt"
    ),
    re_path(
        r"^prompt/(?P<pk>\d+)/delete/$",
        DeletePromptView.as_view(),
        name="delete_prompt",
    ),
    # ModelProviderAPI Urls
    re_path(
        r"^api/(?P<pk>\d+)/$", ModelProviderAPIDetailView.as_view(), name="api_detail"
    ),
    re_path(r"^api/$", ModelProviderAPIListView.as_view(), name="api_list"),
    re_path(r"^api/create/$", CreateModelProviderAPIView.as_view(), name="create_api"),
    re_path(
        r"^api/(?P<pk>\d+)/update/$",
        EditModelProviderAPIView.as_view(),
        name="update_api",
    ),
    re_path(
        r"^api/(?P<pk>\d+)/delete/$",
        DeleteModelProviderAPIView.as_view(),
        name="delete_api",
    ),
    # OpenAIChatQuery Urls
    re_path(
        r"^openai_chat_query/(?P<pk>\d+)/$",
        OpenAIChatQueryDetailView.as_view(),
        name="openai_chat_query_detail",
    ),
    re_path(
        r"^openai_chat_query/$",
        OpenAIChatQueryListView.as_view(),
        name="openai_chat_query_list",
    ),
    re_path(
        r"^openai_chat_query/create/$",
        CreateOpenAIChatQueryView.as_view(),
        name="create_openai_chat_query",
    ),
    re_path(
        r"^openai_chat_query/(?P<pk>\d+)/$",
        OpenAIChatQueryDetailView.as_view(),
        name="openai_chat_query_detail",
    ),
    re_path(
        r"^openai_chat_query/(?P<pk>\d+)/update/$",
        EditOpenAIChatQueryView.as_view(),
        name="update_openai_chat_query",
    ),
    re_path(
        r"^openai_chat_query/(?P<pk>\d+)/delete/$",
        DeleteOpenAIChatQueryView.as_view(),
        name="delete_openai_chat_query",
    ),
]
