FROM python:3.6.3-alpine3.6
COPY ./requirements.txt /
RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["python"]
CMD ["app.py"]
