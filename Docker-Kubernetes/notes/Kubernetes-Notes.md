### Overview:

- Kubernetes (Also known as K8s)
- Created at Google
- Released July 2015
- 3rd gen container scheduler from Google
- Google donated it to the CNCF
- Currently the leading orchestration tool
- Designed as a loosley couples collection of components centered around deploying, maintaining and scaling workloads.
- Vendor-neutral (Not attached to single company)
- Backed by huge community

### Kubernetes capabilites:

- Service discovery and load balancing
- Storage orchestration (local/cloud)
- Automated rollouts and rollbacks
- Can monitor health of containers
- Secret and config management

### What Kubernetes is NOT used for:

- Building / deploying source code
- Building an application- Does not provide app-level services such as busses, dbs, caches, etc.

### K8s Architecture:

- Kubernetes Master Node (Control plane)
  - Runs K8 services
- Worker Nodes

  - Runs containers that you will deploy in the cluster

- Container runs in pod, pod runs in a node, and nodes form a cluster
  - Cluster [ Node [ Pod [ Container]]]

### Local K8s:

- Requires virtualization

  - Docker Desktop (Limited to one node)
  - MicroK8s (Multiple nodes)
  - Minikube (Multiple nodes)
    - Does not require Docker Desktop
    - Installs on Linux, macOS and Windows
    - Hypervisor like VB is required

- Runs over Docker Desktop

  - Kind (Extra functionalites, Multiple nodes)
    - Multiple nodes
    - High Availability Control Plane
    - Define in YAML

- Docker Desktop is currently the only way to run both Linux and Windows containers
- Docker Desktop runs on Hyper-V or WSL 2

### K8s CLI & Context:

- K8s API:
  - On master node
  - Exposes a rest api which is also the only point of comminication for k8 clusters
    - Can set/get state
- CLI:
  - Called kubectl
  - Communicates with the api server
  - Configuration stored locally (under the .kube folder)
- Context:
  - A group of access parameters to a K8s cluster
  - Container a cluster, a user, and a namespace
  - Current context is the cluster that is currently the default for kubectl.
    - All kubectl commands run against that cluster
  - Kubectx - Quickly switch context
    - Instead of typing: kubectl config use-context minikube
    - Simply type: kubextz [contextName]

### Declarative / Imperative

- Imperative
  - Use kubextl commands, issue a series of commands to create resources
  - Great for learning, testing and troubleshooting
  - It's like code
- Declarative

  - Using kubectl and YAML manifests defining the resources that you need
  - Reproducible, repeatable
  - Can be saved in source control
  - Data that can be parsed/modded

- Imperative:

```
kubectl run mynginx --image=nginx -- port=80
kubectl create deploy mynginx --image=nginx --port=80 --replacas=3
kubectl create service nodeport myservice --targetPort=8080
kubectl delete pod nginx
```

- Declarative:
- Use a YAML file to define the resouce then send the content of the file to the cluster to create the resources.

### YAML

- Root level required props
  - apiVersion: Api version of obj
  - kind: type of obj
  - metadata.name: unique name for obj
  - metadata.namespace: scoped env name
  - spec: obj spec or desired state
- Create an obj using YAML: kubectl create -f [YAML file]
