# This Dockerfile builds the API only.

FROM python:slim

RUN useradd memsum

WORKDIR /home

COPY memsum-api ./
CMD ["cd", "memsum-api"]
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP memsum-app.py
ENV FLASK_DEBUG 0

RUN chown -R memsum:memsum ./
USER memsum

EXPOSE 5000
#CMD ["gunicorn", "-b", ":5000", "api:app"]
ENTRYPOINT ["./boot.sh"]