FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
EXPOSE 5000
WORKDIR /app
RUN pip install flask
COPY . .
CMD ["flask","run","--host","0.0.0.0"]