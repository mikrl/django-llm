from setuptools import setup, find_packages

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="django-llm",
    version="0.1.0",
    author="Michael Lynch",
    author_email="michael@flatlander.dev",
    description="A LLM (Large Language Model) app for Django",
    url="https://github.com/mikrl/django-llm",
    license="MIT",
    packages=find_packages(exclude=["django_llm", "tests"]),
    install_requires=requirements, 
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4",
        "Framework :: Django :: 4.1",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Software Development :: User Interfaces",
    ],
)
