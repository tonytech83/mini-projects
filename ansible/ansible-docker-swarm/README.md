- Craete infrastructure (use terraform\proxmox-vms)
```sh
# check the manifests
terraform plan

# apply the manifests
terraform apply

# destroy 
terraform destroy
```

- Run bootstrap.yaml playbook creates the `ansible` user with copy the ssh key. Craete ssh key before this step.
```sh
ansible-playbook bootstrap.yaml \
    --key-file ~/.ssh/ansible-ssh-key \
    -e "ansible_user=root"
```
- Check if `ansible` user is redy.
```sh
ansible all -m ping
```
- Create Docker Swarm.
```sh
ansible-playbook site.yaml
```
