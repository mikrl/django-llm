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

    def do_query(self, **variables):
        openai_api_key = self.api.api_key
        provider = ChatOpenAI(openai_api_key=openai_api_key)

        input_vars = self.prompt.as_dict().get("variables")

        template = self.prompt.template
        prompt = PromptTemplate(input_variables=input_vars, template=template)

        chain = LLMChain(llm=provider, prompt=prompt)
        return chain.run(**variables)

    def do_query_dict(self, **variables):
        return {
            "id": self.id,
            "prompt": self.prompt.as_dict(),
            "promptvars": self.prompt.variables,
            "suppliedvars": variables,
            "queryresponse": self.do_query(**variables),
        }

    def update(self, new_prompt: Prompt):
        self.update(new_prompt)

    def __str__(self):
        return str(self.id)
