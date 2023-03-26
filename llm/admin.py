from django.contrib import admin

from llm.models import ModelProviderAPI
from llm.models import Prompt
from llm.models.queries import OpenAIChatQuery

# Register your models here.
admin.site.register(ModelProviderAPI)
admin.site.register(Prompt)
admin.site.register(OpenAIChatQuery)
