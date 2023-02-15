FROM python:3.10

EXPOSE 8000
WORKDIR /server_source/

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev \
  && apt-get install -y gettext \
  && apt-get install -y gcc curl dos2unix

RUN curl https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh -o /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

COPY ./requirements/requirements.dev.txt /requirements.dev.txt
RUN pip install -U pip && pip install -r /requirements.dev.txt

COPY ./docker/development/server/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh && dos2unix /entrypoint.sh

COPY ./docker/development/server/start.sh /start.sh
RUN chmod +x /start.sh && dos2unix /start.sh

ENTRYPOINT ["bash", "/entrypoint.sh"]
