# Build stage
FROM python:3.10-alpine AS builder

WORKDIR /root

COPY ./pdfsvc/requirements.txt .

RUN apk add --no-cache make gcc g++ musl-dev python3-dev postgresql-dev
RUN apk add --no-cache pango zlib-dev jpeg-dev libffi-dev openjpeg-dev
RUN pip install --no-cache-dir --user -r requirements.txt

# Final image
FROM python:3.10-alpine

WORKDIR /opt/pdfsvc

RUN apk add --no-cache unit-python3 curl postgresql-client pango zlib jpeg openjpeg font-noto msttcorefonts-installer

COPY --chown=unit --from=builder /root/.local /opt/.local
ENV PATH=/opt/.local/bin:$PATH
ENV PYTHONPATH=/opt/.local/lib/python3.10/site-packages:$PYTHONPATH

COPY --chown=unit ./pdfsvc .
COPY ./django.unit.json ./django-entrypoint.sh /docker-entrypoint.d/
COPY ./unit-docker-entrypoint.sh /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/unit-docker-entrypoint.sh"]

CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]