FROM python:3.6.3-jessie
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN python -v
RUN pip -v
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
