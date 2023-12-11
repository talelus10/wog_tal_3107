FROM python:alpine
RUN pip install flask
WORKDIR /app
COPY . /app
EXPOSE 8777 5000
CMD python main_score.py
