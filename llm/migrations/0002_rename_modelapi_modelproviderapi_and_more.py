# Generated by Django 4.1.7 on 2023-03-24 04:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("llm", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="ModelAPI",
            new_name="ModelProviderAPI",
        ),
        migrations.AlterModelOptions(
            name="modelproviderapi",
            options={
                "verbose_name": "LLM Provider API",
                "verbose_name_plural": "LLM Provider APIs",
            },
        ),
        migrations.AlterModelOptions(
            name="prompt",
            options={"verbose_name": "Prompt", "verbose_name_plural": "Prompts"},
        ),
        migrations.AlterField(
            model_name="prompt",
            name="input_variables",
            field=models.CharField(max_length=4096, verbose_name="Input Variables"),
        ),
    ]