# Minikube
## Setting up the environment
minikube start

### Show the dashboard
minikube dashboard

### Ensure that the docker command refers to the one in the minikube VM
eval $(minikube docker-env)     

## Deployments (container descriptions with resource requirements)
kubectl create -f frontend-deployment.yaml
kubectl delete -f frontend-deployment.yaml

### Force deployment updates (to use together with `docker build` and `minikube service`)
kubectl replace -f frontend-deployment.yaml --force

## Services
kubectl create -f frontend-service.yaml
kubectl delete -f frontend-service.yaml

### Alternatively, there exists a loadbalance service
kubectl expose deployment frontend-deployment --type=LoadBalancer --port=8080


kubectl get services

martijn@martijn-laptop  ~/Software/k8s/flask/frontend $  kubectl get services                   
NAME                  TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
frontend-deployment   LoadBalancer   10.110.9.246    <pending>     8080:30749/TCP   2m12s
frontend-service      NodePort       10.107.236.11   <none>        5001:31843/TCP   10s
kubernetes            ClusterIP      10.96.0.1       <none>        443/TCP          113m

minikube service frontend-service

Somehow the one with the LoadBalancer doesn't correctly connect up



# Docker
## Building a docker container
docker build -t martijn-flask-frontend:1.0 .

## Showing the available docker images
docker images

## Running a docker container
(Note that if you do this from the minikube VM you won't be able to access it)
docker run -p 5001:5001 martijn-flask-frontend:1.0