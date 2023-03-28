from langchain.prompts import PromptTemplate
from langchain.chat_models.openai import ChatOpenAI
from langchain.chains import LLMChain

from django.db import models
from llm.models import ModelProviderAPI
from llm.models import Prompt


class OpenAIChatQuery(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    prompt = models.OneToOneField(Prompt, on_delete=models.CASCADE)
    api = models.ForeignKey(ModelProviderAPI, on_delete=models.SET_NULL, null=True)
    memory = models.BooleanField()

    def do_query(self, **variables):
        openai_api_key = self.api.api_key
        provider = ChatOpenAI(openai_api_key=openai_api_key)

        input_vars = self.prompt.to_json().get("variables")

        template = self.prompt.template
        prompt = PromptTemplate(input_variables=input_vars, template=template)

        chain = LLMChain(llm=provider, prompt=prompt)
        return chain.run(**variables)

    def json_response(self, **variables):
        return {
            "id": self.id,
            "prompt": self.prompt.to_json(),
            "promptvars": self.prompt.variables,
            "suppliedvars": variables,
            "response": self.do_query(**variables),
        }

    def update(self, instance, new_prompt: Prompt):
        instance.update(new_prompt)

    def __str__(self):
        return str(self.id)
