FROM ubuntu:bionic

RUN apt-get update --fix-missing && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
      openssl \
      libssl1.0.0 \
      python \
      python-pip \
    && apt-get clean

EXPOSE 5684

WORKDIR /usr/src/app

RUN openssl version

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

