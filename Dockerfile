# Pull base image
FROM python:3.9

# Get environment varibles
ARG DEBUG

# Set environment varibles
ENV POETRY_VERSION=1.1.12
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /src/

COPY ./src/ /src/

# Poetry install
RUN apt-get update \
&& apt-get autoclean && apt-get autoremove \
&& rm -rf /var/lib/apt/lists/* \
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  \
&& pip install "poetry==$POETRY_VERSION" \
&& poetry config virtualenvs.create false

RUN poetry install


EXPOSE 8000