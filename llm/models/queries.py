from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain

from django.db import models
from llm.managers.openai import OpenAIChatManager
from llm.models import ModelProviderAPI
from llm.models import Prompt


class OpenAIChatQuery(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    prompt = models.OneToOneField(Prompt, on_delete=models.CASCADE)
    api = models.ForeignKey(ModelProviderAPI, on_delete=models.SET_NULL, null=True)
    memory = models.BooleanField()
    objects = OpenAIChatManager()

    def do_query(self, **variables):
        openai_api_key = self.api.api_key
        provider = ChatOpenAI(openai_api_key=openai_api_key)

        input_vars = self.prompt.to_json().get("variables")

        template = self.prompt.template
        prompt = PromptTemplate(input_variables=input_vars, template=template)

        chain = LLMChain(llm=provider, prompt=prompt)
        return chain.run(**variables)

    def __str__(self):
        return str(self.id)
