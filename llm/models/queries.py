from django.db import models
from llm.managers.openai import OpenAIChatManager
from llm.models import ModelProviderAPI
from llm.models import Prompt

from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain


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

        # Iterates over input vars from the database and pulls vals from keyword args
        # Defaults to the empty string # TODO add validation logic
        var_dict = {var: variables.get(var, "") for var in input_vars}

        template = self.prompt.template
        if self.memory:
            # TODO manage max length
            template = f"{self.query_response}\n{template}"
        prompt = PromptTemplate(input_variables=input_vars, template=template)

        chain = LLMChain(provider, prompt)
        self.query_response = chain.run(var_dict)

    def __str__(self):
        return str(self.id)
