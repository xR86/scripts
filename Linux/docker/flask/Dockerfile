FROM alpine:3.6 
 
#RUN apt-get update -y 
#RUN apt-get install -y python-pip python-dev build-essential 
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  #&& pip install virtualenv \ 
  && rm -rf /var/cache/apk/* 
 
#WORKDIR /app 
COPY . /app 
#ONBUILD COPY . /app 

RUN pip install -r /app/requirements.txt 
 
EXPOSE 8080 
 
#ENTRYPOINT ["python"] 
#CMD ["app.py"] 
CMD ["python", "app/app.py"] 