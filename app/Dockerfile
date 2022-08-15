FROM python:3.8-slim-buster
RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential netcat\
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*
RUN adduser --home /app --system --group user
WORKDIR /app
COPY --chown=user:user app .
RUN pip install -r requirements.txt 
USER user
ENV PYTHONUNBUFFERED=1
ENTRYPOINT ["gunicorn"]



