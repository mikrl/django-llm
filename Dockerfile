FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install django-llm

RUN django-admin startproject django_llm .
# Add 'llm' to INSTALLED_APPS in settings.py
RUN sed -i '/INSTALLED_APPS/s/\[/\[\n    "llm",/' django_llm/settings.py

RUN ./manage.py migrate

# Run manage.py shell
CMD ["./manage.py", "shell"]
