
# ###########
# # BUILDER #
# ###########

FROM python:3.10-slim  as build

ENV TZ="America/Sao_Paulo" PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=random PIP_NO_CACHE_DIR=off PIP_DISABLE_PIP_VERSION_CHECK=on
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

# #########
# # FINAL #
# #########

FROM python:3.10-slim

WORKDIR /usr/app

COPY --from=build /usr/app/venv ./venv
COPY . .

ENV PATH="/usr/app/venv/bin:$PATH"

#EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--debug", "--workers", "3"]





#
## ###########
## # BUILDER #
## ###########
#
#FROM python:3.9.10-slim-buster AS compile-image
##FROM python:3.9.10-slim AS compile-image
##FROM python:3.9.10-alpine AS compile-image
##FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-slim AS compile-image
#
## set work directory
##WORKDIR /code
#
## set environment variables
#ENV TZ="America/Sao_Paulo" PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=random PIP_NO_CACHE_DIR=off PIP_DISABLE_PIP_VERSION_CHECK=on
#
## install system dependencies
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends build-essential gcc
#
## install app dependencies
#RUN pip install --upgrade pip
#RUN pip install --upgrade 'setuptools >=14.0'
#RUN pip3 install fastapi
#RUN pip install "uvicorn[standard]"
#RUN pip3 install pytest
#RUN pip3 install pytest-cov
#
## # install python dependencies
## COPY ./requirements.txt /code/requirements.txt
## RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
## #########
## # FINAL #
## #########
#
##FROM python:3.9.10-slim AS build-image
#FROM python:3.9.10-slim-buster AS build-image
#
## # create the appropriate directories
#WORKDIR /code
#
## copy only the dependencies installation from the 1st stage image
##COPY --from=compile-image /code /code
##COPY . /code
#
## update PATH environment variable
#ENV PATH=/root/.local:$PATH
#
#EXPOSE 80
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--debug"]












## ###########
## # BASE #
## ###########
#
#FROM python:3.9.10-alpine as base
#
## ###########
## # BUILDER #
## ###########
#
#FROM base as builder
#WORKDIR /code
#ENV TZ="America/Sao_Paulo" PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=random PIP_NO_CACHE_DIR=off PIP_DISABLE_PIP_VERSION_CHECK=on
#RUN pip install --upgrade pip
#RUN pip install --upgrade 'setuptools >=14.0'
#COPY ./requirements.txt /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#COPY . /code
#
## #########
## # FINAL #
## #########
#
#FROM base
#WORKDIR /code
#COPY --from=builder /code /usr/local
#COPY . /code
##COPY --from=builder /code /code
##COPY . .
#EXPOSE 80
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--debug"]

#
## Stage 1 - Install build dependencies
#FROM python:3.9.10-alpine AS builder
#WORKDIR /app
#RUN pip install --upgrade pip
#RUN pip install --upgrade 'setuptools >=14.0'
##RUN python -m venv .venv && .venv/bin/pip install --no-cache-dir -U pip setuptools
##COPY ./requirements.txt /app/requirements.txt
##RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#
## Stage 2 - Copy only necessary files to the runner stage
#FROM python:3.9.10-alpine
#WORKDIR /app
#COPY --from=builder /app /app
#COPY . /app
#ENV PATH="/app/.venv/bin:$PATH"
#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload", "--debug"]