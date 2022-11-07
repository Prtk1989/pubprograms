'''
Publishing Services (ServiceTypes)

For some parts of your application (for example, frontends) you may want to expose a Service onto 
an external IP address, that's outside of your cluster.

Kubernetes ServiceTypes allow you to specify what kind of Service you want. The default is 
ClusterIP.

Type values and their behaviors are:

ClusterIP: Exposes the Service on a cluster-internal IP. Choosing this value makes the Service 
only reachable from within the cluster. This is the default ServiceType.

NodePort: Exposes the Service on each Node's IP at a static port (the NodePort). 
A ClusterIP Service, to which the NodePort Service routes, is automatically created. 
You'll be able to contact the NodePort Service, from outside the cluster, 
by requesting <NodeIP>:<NodePort>.

LoadBalancer: Exposes the Service externally using a cloud provider's load balancer. 
NodePort and ClusterIP Services, to which the external load balancer routes, are automatically 
created.

ExternalName: Maps the Service to the contents of the externalName field (e.g. foo.bar.example.com),
 by returning a CNAME record with its value. No proxying of any kind is set up.

Note: You need either kube-dns version 1.7 or CoreDNS version 0.0.8 or higher to use the 
ExternalName type.

You can also use Ingress to expose your Service. Ingress is not a Service type, but it acts 
as the entry point for your cluster. It lets you consolidate your routing rules into a single 
resource as it can expose multiple services under the same IP address.

