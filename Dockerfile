FROM continuumio/miniconda3
WORKDIR /opt/WebServices001/Pcbd002/
COPY WebServices001/* ./
RUN apt-get update && apt-get install net-tools -y && apt-get install emacs-nox -y && apt-get install procps -y
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]