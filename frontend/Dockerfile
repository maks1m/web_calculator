FROM python:3.11-slim as base
RUN adduser --disabled-password reflex

FROM base as runtime
RUN apt-get update \
    && apt-get install -y gcc g++ python3-dev curl \
    && curl -fsSL https://deb.nodesource.com/setup_19.x | bash - \
    && apt-get update \
    && apt-get install -y nodejs unzip \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://bun.sh/install | bash
RUN pip install --no-cache-dir wheel

FROM runtime as build
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt


FROM build as init

WORKDIR /app
COPY . .

USER reflex

# CMD ["reflex", "init"]
#CMD ["reflex", "run", "--env", "prod"]
CMD ["reflex","run"]

EXPOSE 3000
EXPOSE 8000
