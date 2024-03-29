#tiangolo/uwsgi-nginx-flask
FROM continuumio/miniconda3
COPY flask001/ ./
ADD flask001/application .
ADD flask001/__pycache__ ./
RUN apt-get update && apt-get install net-tools emacs-nox procps netcat nmap tcpdump curl build-essential python-dev python3 uwsgi-core libpcre3 libffi-dev nginx -y
RUN pip install --upgrade pip && pip install -r requirements.txt && rm -v /etc/nginx/nginx.conf && mkdir /etc/nginx/logs
#ADD NginexAuto001/ /NginexAuto001
ADD testlog_1/ /testlog_1
ADD testlog_2/ /testlog_2
ADD nginx.conf /etc/nginx/
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
# Create a runner script for the entrypoint
COPY runner.sh /runner.sh
RUN chmod +x /runner.sh
# Expose ports
EXPOSE 5000
ENV FLASK_APP='main.py'
RUN rm -fr __init__.py && printf "Running Flask...!\n"
#ENTRYPOINT ["/runner.sh"]
# Set the default command to execute
CMD ["flask", "run", "--host=0.0.0.0"]
