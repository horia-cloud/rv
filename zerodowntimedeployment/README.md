On a high level the automated process looks something like this in pseudo-code:

trigger deployment  
for_each instance  
  send shutdown signal
  remove from loadbalancer
  wait for shutdown
  remove old version
  spin up new version
  wait for startup
  add to loadbalancer
done


One big reason to use containers is the fact that pretty much all container orchestrators have a built-in process of rolling deployment.

Kubernetes with rolling updates:
https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/



For demo purposes:
docker rm -f my-service docker run -d --name my-service my_service:v2
