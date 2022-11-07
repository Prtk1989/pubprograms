
#How to check kubernetes service is up or not
---------------------------------------------

'''
kubectl get svc

1. #works for http services
wget <servicename>:<httpport>

#Confirm there is a DNS entry for the service!
nslookup <servicename>

2. Alternatively, you can port forward to your local machine and test locally.

kubectl port-forward <service_name> 8000:8080

You can now address the service as localhost:8000.

3. kubectl describe service <service-name> | grep Endpoints

You should see IPs of all the pods related to the workload listed. 

4. Make sure the selector in the K8s service matches the pods’ labels!

kubectl get pods --show-labels
kubectl describe svc <service_name>

all the pods should show the same label as the service label

5. Finally, make sure that the code in your pods actually listens 
to the targetPort you specified for the service

6. kubectl get endpoints ${SERVICE_NAME}

Make sure that the endpoints match up with the number of pods that you expect 
to be members of your service. For example, if your Service is for an nginx 
container with 3 replicas, you would expect to see three different IP addresses 
in the Service's endpoints.

7. ingress rules for service
If you have deployed any Network Policy Ingress rules which may affect incoming traffic to 
servicename-* Pods, these need to be reviewed.

8.

Is the Service defined correctly?
It might sound silly, but you should really double and triple check that your Service 
is correct and matches your Pod's port. Read back your Service and verify it:

kubectl get service hostnames -o json
{
    "kind": "Service",
    "apiVersion": "v1",
    "metadata": {
        "name": "hostnames",
        "namespace": "default",
        "uid": "428c8b6c-24bc-11e5-936d-42010af0a9bc",
        "resourceVersion": "347189",
        "creationTimestamp": "2015-07-07T15:24:29Z",
        "labels": {
            "app": "hostnames"
        }
    },
    "spec": {
        "ports": [
            {
                "name": "default",
                "protocol": "TCP",
                "port": 80,
                "targetPort": 9376,
                "nodePort": 0
            }
        ],
        "selector": {
            "app": "hostnames"
        },
        "clusterIP": "10.0.1.175",
        "type": "ClusterIP",
        "sessionAffinity": "None"
    },
    "status": {
        "loadBalancer": {}
    }
}
Is the Service port you are trying to access listed in spec.ports[]?
Is the targetPort correct for your Pods (some Pods use a different port than the Service)?
If you meant to use a numeric port, is it a number (9376) or a string "9376"?
If you meant to use a named port, do your Pods expose a port with the same name?
Is the port's protocol correct for your Pods?


9. Is kube-proxy running?
Confirm that kube-proxy is running on your Nodes. Running directly on a Node, you should 
get something like the below:

ps auxw | grep kube-proxy
root  4194  0.4  0.1 101864 17696 ?    Sl Jul04  25:43 /usr/local/bin/kube-proxy --mas

Next, confirm that it is not failing something obvious, like contacting the master. To do this, 
you'll have to look at the logs. Accessing the logs depends on your Node OS. On some OSes 
it is a file, such as /var/log/kube-proxy.log, while other OSes use journalctl to access logs.


