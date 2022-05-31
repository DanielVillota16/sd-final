# Final project for distributed systems course
Jesus Daniel Villota - A00356255

## Context
Web browser app that stores a value on a redis database through an API.

The app is deployed on Kubernetes and packaged using Helm.

The final Kubernetes arquitecture looks somewhat like this:

![k8s-arc](https://user-images.githubusercontent.com/47828441/171091245-f1de3919-147f-4737-a7b6-fe426d00f610.png)

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
![image](https://user-images.githubusercontent.com/47828441/171087672-fcbc74ae-04ae-4244-a6f1-8d54873f5344.png)

---
![image](https://user-images.githubusercontent.com/47828441/171088015-668f2abb-d71f-4339-82e0-b20a996e5883.png)

---
![image](https://user-images.githubusercontent.com/47828441/171088111-27537a92-4e64-465c-bb14-e91c535971b7.png)

---
![image](https://user-images.githubusercontent.com/47828441/171087763-51c6f8cb-7a95-4d1b-acfd-d5f47e76b495.png)

---
![image](https://user-images.githubusercontent.com/47828441/171089250-c5c560f6-a528-41f8-a9be-dd5337381a57.png)
