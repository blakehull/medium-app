FROM python:3.7-slim

LABEL app.name="related-tags" \
      app.type="api"

ARG PLATFORM=word2vec
ARG NAME=related-tages
ARG VERSION=1

RUN apt-get update
RUN apt-get -y install build-essential

ADD requirements.txt /requirements.txt

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# removes linux due to twistlock vulnerabilities
RUN apt-get -y remove linux-libc-dev

COPY core /core
COPY boot.sh /boot.sh

ARG ENV=production

ENV PORT=8080
ENV HOST=0.0.0.0

ENV INDEX_PATH=/

RUN echo "What is in my docker?: ${INDEX_PATH}" \
    && ls -lh ${INDEX_PATH} \
    && chmod 755 boot.sh

EXPOSE 8080
CMD ["./boot.sh"]