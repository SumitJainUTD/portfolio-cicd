FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code

EXPOSE 80
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:80" ]