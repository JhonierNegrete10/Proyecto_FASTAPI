#pull official base image
FROM python:3.8-slim-buster

# WORKDIR /app/

# RUN apt-get update \
#   && apt-get -y install libpq-dev python-dev \
#   && apt-get -y install build-essential

# # install python dependencies
# RUN pip install --upgrade pip
# RUN pip install -U setuptools

# # COPY ./requirements.txt .
# # RUN pip install -r requirements.txt
# RUN pip install celery

# # COPY ./start.sh /start.sh
# # RUN chmod +x /start.sh

# COPY ./app/celerys /app/celerys
# ENV PYTHONPATH=/app
# EXPOSE 80

# CMD ["celery -A workers worker -l INFO "]