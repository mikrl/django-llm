from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="django-llm",
    version="",
    author="Michael Lynch",
    author_email="michael@flatlander.dev",
    description="A LLM (Large Language Model) app for Django",
    url="<package URL>",
    license="<package license>",
    packages=["django_llm"],
    install_requires= requirements, #TODO test down to Django 3
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: <license name>",
        "Operating System :: OS Independent",
    ],
)