# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Virtual Machine (VM)

Cost: Higher, since you pay for the full VM even when idle
Scalability: Manual scaling; requires creating or resizing VMs
Availability: Depends on manual configuration (load balancers, backups)
Workflow: Requires OS setup, patching, security updates, and server maintenance

App Service
Cost: Lower for small to medium apps; pay-as-you-use model
Scalability: Built-in automatic scaling
Availability: High availability managed by Azure
Workflow: Simple deployment with no server management required

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
Chosen Solution: App Service

App Service was chosen because it provides a managed platform ideal for deploying a Flask web application quickly and efficiently.

Justification
Lower operational cost
Easy deployment directly from source code
Built-in scaling and high availability
No need to manage servers or OS updates
Integrated monitoring and logging

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 
A Virtual Machine would be preferred if the application required:
    Full control over the operating system or custom software installation
    Specialized configurations not supported by App Service
    Running multiple services or background processes on the same server
    Handling very large workloads requiring custom infrastructure tuning
For the current CMS application, these requirements are not necessary, making App Service the most suitable choice.