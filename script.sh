#!/bin/bash

minikube start
helm install my-redis -f ./redis/values.yaml bitnami/redis > /dev/null
helm install final-project ./final-project > /dev/null
minikube addons enable ingress > /dev/null
echo
echo "Wait 60 seconds till everything gets up and ready..."
sleep 60

# SMOKE TEST

curl http://$(minikube ip)/highest
curl http://$(minikube ip)/updatehighest/5142
curl http://$(minikube ip)/highest
