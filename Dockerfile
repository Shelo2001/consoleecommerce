FROM python:3
COPY app.py /
RUN pip install collections
CMD [ "python", "./app.py" ]