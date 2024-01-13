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

### Namespaces

- Allow you to group resouces: Dev, Test, Production (Examples)
  - kind of like logical folders
- K8 creates a default workspace called workspace
- Can cross access namespace objects
- Deleting a namespace will delete all associated child objects

### Master Nodes

- Masternode/Control plane
  - Here lies the k8 controller/services
  - Usually don't run your app containers on master
  - etcd is a key/value datastgore where the state of the cluster is stored. Single source of truth/
- kube-apiserver
  - REST interface
  - Save state to datastore (etcd)
  - All clients interact with it, they will never go directly to the datastore.
- kube-control-manager
  - controller of controllers
  - it runs
    - node controller
      replication controller
      endpoints controller
      service account and token controllers
- cloud-control-manager
  - interact with the cloud providers controllers
    - Node, route, service, volume
- kube-scheduler
  - watches for newly created pods with no node assigned. It will select a node for them to run on
  - Takes into account several factors for scheduling decisions including resource reqs, data locality, affinity, etc.

### Worker nodes

- kubelet
  - manages the pod lifecycle and ensures containers are running/healthy
- kube-proxy
  - network proxy, manages rules on nodes, all network traffic goes through it
- container runtime
  - found on each node, can create a space to run specified containers
- Node pool
  - Group of virtual machines, all with the same size
  - A cluster can have multiple node pools
    - Eachpool can be autoscaled independently
  - Docker Desktop limited to one node.

### Pods

- Atomic unit of the smallest unit of work of K8s
- Encapsulates an app's containers
- Represents a unit of deployment
- pods can run one or multiple containers
- containers within a pod share ip address, mounted volumes
  - communicate via localhost within the pod
- Pods are ephemeral
- Deploying a pod is an atomic op, it succeeds or fails
  - if faulure it is replaced with a new one with a new IP
  - you never update a pod, you replace it with a new version
- Scale by adding more pods, not more containers within a pod
- A node can run many pods, and a pod can run one or more containers

- Normal architecture includes a container within the pod that is the main worker, and then helper containers.

### Pod lifecyle

- Pod Creation:
  - API Server -> etcd -> Scheduler -> Kubelet -> Runtime
- Pod Deletion:
  - API Server -> etcd -> Kubelet -> Runtime -> endpoint controller

### Pod State

- Pending: Accepted but not yet created
- Running: Bound to a node
- Succeeded: Exited with status 0
- Failed: Exited with non 0
- Unknown: Communication issue with pod
- CrashLoopBackOff: Started, crashed, started, crashed again

### Init Containers

- Inits a pod before an application container runs
  - Upon completion of init container job, we can then start real app.
- Always run to completion
- Each init container must complete successfully before next
- If it fails, the kubelet will repeatedly restart it until it succeeds (assuming restartPolicy is NOT set to Never)
- Probes not supported

### Selectors

- Labels: key value pairs used to identify, describe and group related sets od obj/resources.
- Selectors use these labels to filter/select objects.

Example:

```
metadata:
  name: myapp-pod
  labels:
    app: myapp
    type: front-end
spec:
  containers:
  - name: nginx-container
    image: nginx
  nodeSelector:
    disktype: superfast
```

- Can think of them sort of like a SQL query.

```
Select * from Nodes where disktype = superfast
```
