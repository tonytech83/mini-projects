terraform {
  required_providers {
    proxmox = {
      source  = "bpg/proxmox"
      version = "~> 0.111.0"
    }
  }
}

provider "proxmox" {
  endpoint = "https://10.50.0.10:8006"
  username = var.virtual_environment_username
  password = var.virtual_environment_password
  insecure = true
}

resource "proxmox_download_file" "debian_cloud" {
  content_type = "iso"
  datastore_id = "local"
  node_name    = "pve01pr"
  url          = "https://cloud.debian.org/images/cloud/trixie/latest/debian-13-genericcloud-amd64.qcow2"
  file_name    = "debian-13-cloud.img"
}

locals {
  vms = {
    "debian-01" = { vm_id = 201, ip = "10.20.10.101/16", tags = ["pve1", "vm", "test"] }
    "debian-02" = { vm_id = 202, ip = "10.20.10.102/16", tags = ["pve1", "vm", "test"] }
    "debian-03" = { vm_id = 203, ip = "10.20.10.103/16", tags = ["pve1", "vm", "test"] }
    "debian-04" = { vm_id = 204, ip = "10.20.10.104/16", tags = ["pve1", "vm", "test"] }
    "debian-05" = { vm_id = 205, ip = "10.20.10.105/16", tags = ["pve1", "vm", "test"] }
  }
}

resource "proxmox_virtual_environment_vm" "debian" {
  for_each = local.vms

  name      = each.key
  node_name = "pve01pr"
  vm_id     = each.value.vm_id
  tags      = each.value.tags

  cpu {
    cores = 1
  }

  memory {
    dedicated = 1024
  }

  disk {
    datastore_id = "local-lvm"
    interface    = "virtio0"
    size         = 10
    file_id      = proxmox_download_file.debian_cloud.id
    file_format  = "raw"
  }

  network_device {
    bridge   = "vmbr2"
    vlan_id  = 20
    firewall = false
  }

  initialization {
    ip_config {
      ipv4 {
        address = each.value.ip
        gateway = "10.20.0.1"
      }
    }

    dns {
      servers = ["10.20.0.10"]
      domain  = "home.lab"
    }

    user_account {
      username = "root"
      password = var.vm_password
      keys     = [file("~/.ssh/ansible-ssh-key.pub")]
    }
  }

  operating_system {
    type = "l26"
  }

  boot_order = ["virtio0"]
  started    = true
}
