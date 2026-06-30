output "vm_ips" {
  value = {
    for name, vm in proxmox_virtual_environment_vm.debian :
    name => vm.initialization[0].ip_config[0].ipv4[0].address
  }
}
