FROM python:3.12-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . /usr/src/app/.

RUN pip install --no-cache-dir -r requirements.txt

CMD /usr/src/app/entrypoint.sh