# Final project for distributed systems course
Jesus Daniel Villota - A00356255

## Context
Web browser app that stores a value on a redis database through an API.

The app is deployed on Kubernetes and packaged using Helm.

The final Kubernetes arquitecture looks like this: 

---

## Instructions to get the setup ready

Install **minikube** following the steps described in this tutorial: https://computingforgeeks.com/how-to-install-minikube-on-ubuntu-debian-linux/

Install **helm** following the steps described in this tutorial: https://helm.sh/docs/intro/install/

Then add the bitnami repository:
```
helm repo add bitnami https://charts.bitnami.com/bitnami
```

## Instructions to get the application running

First initialize the minikube cluster:
```
minikube start
```
Then deploy the bitnami redis chart with the apropriate values described in redis/values.yaml:
```
helm install my-redis -f ./redis/values.yaml bitnami/redis
```
Then deploy the app chart:
```
helm install final-project ./final-project
```
Enable ingress addon:
```
minikube addons enable ingress
```

**OR just execute all the steps described above by running the included script :)**
```
./script.sh
```

Now, if we want to try out the app, first wait for at least 60 seconds so the pods and services get ready (not necessary if you used the script) and then get the **Ingress** external IP with the following command:
```
minikube ip
```
Finally just copy/paste the resulting IP in Google Chrome and enjoy!

## Evidence
---
