FROM python:3.9

EXPOSE 8000

RUN apt-get update
RUN apt-get install -y vim
RUN pip install --upgrade pip

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY .docker/requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

# Command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]