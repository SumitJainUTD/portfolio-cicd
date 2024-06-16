FROM python:3

# USER app
ENV PYTHONUNBUFFERED 1
ENV HOSTNAME="0.0.0.0"
ENV NEXT_TELEMETRY_DISABLED=1
# RUN mkdir /db
#RUN chown app:app -R /db

RUN mkdir /code
WORKDIR /code
ADD ./requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code
RUN ls
EXPOSE 8080
CMD [ "python", "./resume/manage.py", "runserver", "0.0.0.0:8080" ]