FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /app-backend
WORKDIR /app-backend
COPY ./requirements.txt /app-backend/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /app-backend/
COPY ./entrypoint.sh /app-backend/