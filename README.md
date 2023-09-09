# Kubenetes

## Minikube


follow instructions to build simple deployments and workload
https://minikube.sigs.k8s.io/docs/start/

start minikube
```bash
minikube start
```

minikube dashboard
```bash
minikube dashboard
```

set Docker env variables to point docker-cli to Docker Engine in minikube
```bash
eval $(minikube docker-env)
```


### Cron Job Example
Build basic Docker image and deploy cron job with the image. 
Change the image tag to the one you want to deploy with.
```bash
docker build -f ./cron-job/Dockerfile -t cron-job-image .
kubectl apply -f cron-job/deployment.yaml 
```

