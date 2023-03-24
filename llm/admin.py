from django.contrib import admin

from llm.models import ModelProviderAPI
from llm.models import Prompt

# Register your models here.
admin.site.register(ModelProviderAPI)
admin.site.register(Prompt)