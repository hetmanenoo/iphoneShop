
FROM python:3.9

# ENV PIP_ROOT_USER_ACTION=ignore
RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /django-app


COPY requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt


COPY . .

# EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]