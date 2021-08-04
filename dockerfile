FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev ffmpeg g++ libwebp-dev
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT ["python"]
CMD ["test.py"]
