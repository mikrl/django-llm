# Generated by Django 4.1.7 on 2023-03-27 02:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("llm", "0005_remove_openaichatquery_query_response_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="prompt",
            name="input_variables",
        ),
        migrations.RemoveField(
            model_name="prompt",
            name="num_input_vars",
        ),
    ]