from django.db import models


class OpenAIChatManager(models.Manager):
    def create(self, data):
        openaichat = self.create(**data)
        return openaichat

    def update(self, instance, data):
        for attr, value in data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()
