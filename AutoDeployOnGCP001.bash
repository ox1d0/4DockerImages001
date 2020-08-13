#/bin/bash
source /home/ox1d0/.bashrc
export HOME='/home/ox1d0/'
export KUBECONFIG='.kube/config'

gcloud auth activate-service-account --key-file=/home/ox1d0/Downloads/serious-ascent-282117-dc3e2dae2ba5.json

printf "$KUBECONFIG\n\n"
printf "Geting the New Imagen From GCP Registry Could Take Some Time ....\n"
#sleep 360
printf "Getting Old Image Tag \t\n\n"
key0ld=$(gcloud container images list-tags gcr.io/serious-ascent-282117/github.com/ox1d0/4dockerimages001 | grep -v DIGEST | head -n 2 | tail -n 1| awk '{print $2}')
printf "Old Image Tag --> $key0ld\n"
keyNew=$(gcloud container images list-tags gcr.io/serious-ascent-282117/github.com/ox1d0/4dockerimages001 | grep -v DIGEST | head -n 1 | awk '{print $2}')
printf "New Image Tag --> $keyNew\n"
printf 'Adding new Key to File In order To Deployment....\n\n\n'
sed -i.bak 's/'"$key0ld"'/'"$keyNew"'/g' /home/ox1d0/Kubernetes001/django017service001.yaml

printf "Chcecking For Control Plain on GCP\n docker image --->  $keyNew added into Kubenetes Cluster (GCP CLoud)...\n\n\n"
gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project serious-ascent-282117 && kubectl get all

#gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project serious-ascent-282117

printf "Deploying New Inmage---> $keyNew\t into Kubernetes_GCP.\n"
gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project serious-ascent-282117 && kubectl create -f  /home/ox1d0/4Brightcove001/4DockerImages001/manifest4app.yaml

printf "Checking for New Deployment:\n"
sleep 5
gcloud container clusters get-credentials cluster-1 --zone us-central1-a --project serious-ascent-282117 && kubectl get all
