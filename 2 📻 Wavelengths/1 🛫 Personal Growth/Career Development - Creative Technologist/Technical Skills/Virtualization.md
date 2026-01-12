# Virtualization
### Virtualization (OBJ 2.2)
Definition: Creation of a virtual resource

A virtual machine is a continuer for an **emulated** **computer** that runs an entire operating system

System Virtual Machine
Complete platform designed to replace an entire physical computer and includes a full desktop/server operating system

Processor Virtual Machine
Designed to only run a single process or application like a virtualized web browser or a simple web server

Virtualization continues to rise in order to reduce the physical requirements for data centers

### Hypervisors (OBJ 2.2)
Definition: Manages the distribution of the physical resources of a host machine (server) to the virtual machines being run (guests)

Type I (Bare metal) - faster and more efficient
Type II (runs from OS)
Application Containerization
A single operating system kernel is shared across multiple virtual machines but each virtual machine receives it’s own user space for programs and data

Containerization allows for rapid and efficient deployment of distributed applications

DOCKER
Parallels Virtuozzo
OpenVZ

### Threats to VM (OBJ 2.2)
VMs are separated from other VMs by default
**VM Escape**
An attack that allows an attacker to break out of a normally isolated VM by interacting directly with the hypervisor

Elasticity allows for scaling up or down to meet user demands

Data Remnants
Contents of a virtual machine that exist as deleted files on a cloud-based server after deprovisioning of a virtual machine

Privilege Elevation
Occurs when a user is able to grant themselves the ability to run functions as a higher-level user

Live Migration
Live migration occurs when a VM is moved from one physical server to another over the network.
Susceptible to Man in the middle attack

### Securing VMs (OBJ 2.2)
Uses many of the same security as a physical server


- &nbsp;
		1. Update Hypervisor
		1. Limit connectivity between the virtual machine and the hose
		2. Remove any unnecessary pieces of virtual hardware from the virtual machine
		3. Using proper patch management is important to keeping your guest’s operating system secure
		4. Virtualization Sprawl - occurs when virtual machines are created, used, and deployed without proper management overside by the system admins
		5. Enable encryption on virtual machine files