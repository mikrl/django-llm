from setuptools import setup

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="django-llm",
    version="0.1.0",
    author="Michael Lynch",
    author_email="michael@flatlander.dev",
    description="A LLM (Large Language Model) app for Django",
    url="<package URL>",
    license="MIT",
    packages=["django_llm"],
    install_requires=requirements,  # TODO test down to Django 3
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
