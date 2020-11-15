FROM python:3.6.3

ENV MONGO_HOST localhost
ENV MONGO_PORT 27017
ENV SLACK_TOKEN="xoxb-1412473913510-1460447944487-wldDihh7Sq2HvxZKaZzkNSTF"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /odin

COPY ./odinbot.py /odinbot.py
COPY ./odinbot_app.py /odinbot_app.py

CMD [ "python", "/odinbot_app.py" ]
