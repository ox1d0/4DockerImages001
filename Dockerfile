FROM continuumio/miniconda3
WORKDIR /opt/WebServices001/Pcbd002/
COPY WebServices001/* ./
RUN apt-get update && apt-get install net-tools emacs-nox procps netcat nmap tcpdump curl nginx -y
RUN pip install --upgrade pip && pip install -r requirements.txt && rm -v /etc/nginx/nginx.conf && mkdir /etc/nginx/logs

ADD nginx.conf /etc/nginx/
ADD index.html /www/data/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY runner.sh /runner.sh
RUN chmod +x /runner.sh

# Expose ports
EXPOSE 80
ENTRYPOINT ["/runner.sh"]
# Set the default command to execute
# when creating a new container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
