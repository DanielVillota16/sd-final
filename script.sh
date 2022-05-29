#!bin/bash

minikube start
minikube addons enable ingress

helm install my-redis -f ./redis/values.yaml bitnami/redis
helm install final-project ./final-project

# SMOKE TEST
curl http://$(minikube ip)/highest
curl http://$(minikube ip)/updatehighest/5142
curl http://$(minikube ip)/highest
