FROM continuumio/miniconda3
WORKDIR flask001
COPY flask001/ ./
ADD flask001/application .
ADD flask001/__pycache__ ./
RUN apt-get update && apt-get install net-tools emacs-nox procps netcat nmap tcpdump curl nginx -y
RUN pip install --upgrade pip && pip install -r requirements.txt && rm -v /etc/nginx/nginx.conf && mkdir /etc/nginx/logs
ADD NginexAuto001/ ../NginexAuto001
ADD testlog_1/ ../testlog_1
ADD testlog_2/ ../testlog_2
ADD nginx.conf /etc/nginx/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Expose ports
EXPOSE 80
# Set the default command to execute
ENTRYPOINT nginx
# when creating a new container
ENV FLASK_APP='main.py'
ENV MESSAGE "DEPLOYING Flask01"
RUN rm -fr __init__.py && printf "Running Flask...!\n"
ENTRYPOINT flask run 
