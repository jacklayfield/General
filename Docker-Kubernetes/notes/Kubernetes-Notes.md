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
