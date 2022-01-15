FROM python:3.7

LABEL MAINTANER="marcio.lima@santander.com.br"
LABEL NAME="MARCIO DE LIMA"

ENV APP_HOME="/opt/app"
USER root

WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt

COPY . $APP_HOME

ENV LC_ALL=en_US.utf8 \
    LANG=en_US.utf8 \
    APP_HOME=${APP_HOME}

RUN chmod 777 $APP_HOME

EXPOSE 5000
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]

