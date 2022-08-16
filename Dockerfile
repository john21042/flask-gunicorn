FROM python:3.7.3-slim
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY ./app /app
RUN chmod -R +rx /app
COPY ./run.sh /run.sh
RUN chmod +x /run.sh
WORKDIR /app
ENTRYPOINT ["/run.sh"]