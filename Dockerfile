# pull the official base image
FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/marina-portfolio

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /usr/src/marina-portfolio
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/marina-portfolio

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]