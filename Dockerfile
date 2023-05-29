ARG PYTHON_VERSION="3.11.3"

FROM python:${PYTHON_VERSION}-alpine3.18

RUN apk --update add groff

RUN adduser -D nifcloud
USER nifcloud
WORKDIR /home/nifcloud

ENV PATH="/home/nifcloud/.local/bin:${PATH}"

COPY . .
COPY bin/nifcloud /usr/local/bin/nifcloud

RUN pip install pipenv==2021.5.29 --no-cache-dir --user && pipenv install --system --deploy && pip uninstall -y pipenv

ENTRYPOINT ["/usr/local/bin/nifcloud"]
