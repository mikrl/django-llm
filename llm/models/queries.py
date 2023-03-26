from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain

from django.db import models
from llm.managers.openai import OpenAIChatManager
from llm.models import ModelProviderAPI
from llm.models import Prompt


class OpenAIChatQuery(models.Model):
    prompt = models.OneToOneField(Prompt, on_delete=models.CASCADE)
    api = models.OneToOneField(ModelProviderAPI, on_delete=models.SET_NULL, null=True)
    query_response = models.TextField()
    memory = models.BooleanField()
    objects = OpenAIChatManager()

    def do_query(self, **variables):
        openai_api_key = self.api.api_key
        provider = ChatOpenAI(openai_api_key=openai_api_key)

        input_vars = self.prompt.input_variables.split(";")
        # TODO validate whether input vars match the supplied kwargs. Fallback logic

        template = self.prompt.template
        if self.memory:
            # TODO manage max length
            template = f"{self.query_response}\n{template}"
        prompt = PromptTemplate(input_variables=input_vars, template=template)

        chain = LLMChain(provider, prompt)
        self.query_response = chain.run(**variables)

    def __str__(self):
        return str(self.id)
