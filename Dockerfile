FROM python:3
WORKDIR /usr/src/app
COPY . .
RUN pip3 install praw
CMD ["WhatDayIsItToday.py"]
ENTRYPOINT ["python3"]
