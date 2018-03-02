#### 获取主机信息

* action名称

`setup`

* action参数

`空`

* 返回示例

```
{
    "task_id": "123456abc",
    "ok": {
        "39.106.97.235": {
            "ansible_product_serial": "NA",
            "ansible_form_factor": "Other",
            "ansible_distribution_file_parsed": true,
            "ansible_fips": false,
            "ansible_service_mgr": "systemd",
            "ansible_user_id": "rocky",
            "ansible_selinux_python_present": true,
            "ansible_userspace_bits": "64",
            "ansible_ssh_host_key_rsa_public": "AAAAB3NzaC1yc2EAAAADAQABAAABAQDhrdJHAJ2IcYfdFSec6LZFsUhDZpUST2BpCAzuFKD3rKmrTlFpS3fKjODBJQindvDzaRNCboGFL5v1afGIAjyFVUzVWx9x2ygOLxqPi133Z7FWzWoSFTaeoPlv5fozBEqOlfMPmrvutJxCF7yJwvyUY220H4vRM64UJmCE0oCsGNj1XjRAnV05uJzlr8Ck8QvW8gw0S4P3o5JffuuLB9XrRAwdvykbLuCc1svttPgYJ+lOnY0p8wGsRaL8G6SJBE3JJgJlTB+dTjf5m0fkzl8nWcyYnvk5fdCRuANntFpfPeZ2jG6muwdNnLMlDnjGCe+B7/RruSe+Z/g4Qtg2jLbt",
            "gather_subset": [
                "all"
            ],
            "ansible_real_user_id": 1000,
            "ansible_architecture": "x86_64",
            "ansible_local": {},
            "ansible_distribution_version": "7.4.1708",
            "ansible_domain": "",
            "ansible_distribution_file_path": "/etc/redhat-release",
            "ansible_user_shell": "/bin/bash",
            "ansible_date_time": {
                "weekday_number": "3",
                "iso8601_basic_short": "20180228T112019",
                "tz": "CST",
                "weeknumber": "09",
                "hour": "11",
                "year": "2018",
                "minute": "20",
                "tz_offset": "+0800",
                "month": "02",
                "epoch": "1519788019",
                "iso8601_micro": "2018-02-28T03:20:19.388921Z",
                "weekday": "Wednesday",
                "time": "11:20:19",
                "date": "2018-02-28",
                "iso8601": "2018-02-28T03:20:19Z",
                "day": "28",
                "iso8601_basic": "20180228T112019388826",
                "second": "19"
            },
            "ansible_ssh_host_key_ed25519_public": "AAAAC3NzaC1lZDI1NTE5AAAAINDEFleMrI0WEiYdAaNN5wtOEBz2bm6BboBpOSpw4bon",
            "ansible_processor_cores": 1,
            "ansible_virtualization_role": "guest",
            "ansible_distribution_file_variety": "RedHat",
            "ansible_env": {
                "LANG": "en_US.UTF-8",
                "TERM": "xterm-256color",
                "SHELL": "/bin/bash",
                "XDG_RUNTIME_DIR": "/run/user/1000",
                "SHLVL": "2",
                "SSH_TTY": "/dev/pts/0",
                "HOME": "/home/rocky",
                "_": "/usr/bin/python",
                "LC_CTYPE": "zh_CN.UTF-8",
                "LESSOPEN": "||/usr/bin/lesspipe.sh %s",
                "PWD": "/home/rocky",
                "LOGNAME": "rocky",
                "USER": "rocky",
                "MAIL": "/var/mail/rocky",
                "PATH": "/home/rocky/anaconda3/bin:/usr/local/bin:/usr/bin",
                "LS_COLORS": "rs=0:di=38;5;27:ln=38;5;51:mh=44;38;5;15:pi=40;38;5;11:so=38;5;13:do=38;5;5:bd=48;5;232;38;5;11:cd=48;5;232;38;5;3:or=48;5;232;38;5;9:mi=05;48;5;232;38;5;15:su=48;5;196;38;5;15:sg=48;5;11;38;5;16:ca=48;5;196;38;5;226:tw=48;5;10;38;5;16:ow=48;5;10;38;5;21:st=48;5;21;38;5;15:ex=38;5;34:*.tar=38;5;9:*.tgz=38;5;9:*.arc=38;5;9:*.arj=38;5;9:*.taz=38;5;9:*.lha=38;5;9:*.lz4=38;5;9:*.lzh=38;5;9:*.lzma=38;5;9:*.tlz=38;5;9:*.txz=38;5;9:*.tzo=38;5;9:*.t7z=38;5;9:*.zip=38;5;9:*.z=38;5;9:*.Z=38;5;9:*.dz=38;5;9:*.gz=38;5;9:*.lrz=38;5;9:*.lz=38;5;9:*.lzo=38;5;9:*.xz=38;5;9:*.bz2=38;5;9:*.bz=38;5;9:*.tbz=38;5;9:*.tbz2=38;5;9:*.tz=38;5;9:*.deb=38;5;9:*.rpm=38;5;9:*.jar=38;5;9:*.war=38;5;9:*.ear=38;5;9:*.sar=38;5;9:*.rar=38;5;9:*.alz=38;5;9:*.ace=38;5;9:*.zoo=38;5;9:*.cpio=38;5;9:*.7z=38;5;9:*.rz=38;5;9:*.cab=38;5;9:*.jpg=38;5;13:*.jpeg=38;5;13:*.gif=38;5;13:*.bmp=38;5;13:*.pbm=38;5;13:*.pgm=38;5;13:*.ppm=38;5;13:*.tga=38;5;13:*.xbm=38;5;13:*.xpm=38;5;13:*.tif=38;5;13:*.tiff=38;5;13:*.png=38;5;13:*.svg=38;5;13:*.svgz=38;5;13:*.mng=38;5;13:*.pcx=38;5;13:*.mov=38;5;13:*.mpg=38;5;13:*.mpeg=38;5;13:*.m2v=38;5;13:*.mkv=38;5;13:*.webm=38;5;13:*.ogm=38;5;13:*.mp4=38;5;13:*.m4v=38;5;13:*.mp4v=38;5;13:*.vob=38;5;13:*.qt=38;5;13:*.nuv=38;5;13:*.wmv=38;5;13:*.asf=38;5;13:*.rm=38;5;13:*.rmvb=38;5;13:*.flc=38;5;13:*.avi=38;5;13:*.fli=38;5;13:*.flv=38;5;13:*.gl=38;5;13:*.dl=38;5;13:*.xcf=38;5;13:*.xwd=38;5;13:*.yuv=38;5;13:*.cgm=38;5;13:*.emf=38;5;13:*.axv=38;5;13:*.anx=38;5;13:*.ogv=38;5;13:*.ogx=38;5;13:*.aac=38;5;45:*.au=38;5;45:*.flac=38;5;45:*.mid=38;5;45:*.midi=38;5;45:*.mka=38;5;45:*.mp3=38;5;45:*.mpc=38;5;45:*.ogg=38;5;45:*.ra=38;5;45:*.wav=38;5;45:*.axa=38;5;45:*.oga=38;5;45:*.spx=38;5;45:*.xspf=38;5;45:",
                "XDG_SESSION_ID": "1352",
                "SSH_CLIENT": "111.202.106.229 33918 22",
                "SSH_CONNECTION": "111.202.106.229 33918 172.17.61.91 22"
            },
            "ansible_effective_group_id": 1000,
            "ansible_bios_version": "rel-1.7.5-0-ge51488c-20140602_164612-nilsson.home.kraxel.org",
            "ansible_processor": [
                "0",
                "GenuineIntel",
                "Intel(R) Xeon(R) Platinum 8163 CPU @ 2.50GHz"
            ],
            "ansible_virtualization_type": "kvm",
            "ansible_lo": {
                "features": {
                    "tx_checksum_ipv4": "off [fixed]",
                    "generic_receive_offload": "on",
                    "tx_checksum_ipv6": "off [fixed]",
                    "tx_scatter_gather_fraglist": "on [fixed]",
                    "rx_all": "off [fixed]",
                    "highdma": "on [fixed]",
                    "rx_fcs": "off [fixed]",
                    "tx_lockless": "on [fixed]",
                    "tx_tcp_ecn_segmentation": "on",
                    "tx_tcp6_segmentation": "on",
                    "tx_gso_robust": "off [fixed]",
                    "tx_ipip_segmentation": "off [fixed]",
                    "tx_tcp_mangleid_segmentation": "on",
                    "tx_checksumming": "on",
                    "vlan_challenged": "on [fixed]",
                    "loopback": "on [fixed]",
                    "fcoe_mtu": "off [fixed]",
                    "scatter_gather": "on",
                    "tx_checksum_sctp": "on [fixed]",
                    "tx_vlan_stag_hw_insert": "off [fixed]",
                    "rx_vlan_stag_hw_parse": "off [fixed]",
                    "tx_gso_partial": "off [fixed]",
                    "rx_vlan_stag_filter": "off [fixed]",
                    "large_receive_offload": "off [fixed]",
                    "tx_scatter_gather": "on [fixed]",
                    "rx_checksumming": "on [fixed]",
                    "tx_tcp_segmentation": "on",
                    "netns_local": "on [fixed]",
                    "busy_poll": "off [fixed]",
                    "generic_segmentation_offload": "on",
                    "tx_udp_tnl_segmentation": "off [fixed]",
                    "tcp_segmentation_offload": "on",
                    "l2_fwd_offload": "off [fixed]",
                    "rx_vlan_offload": "off [fixed]",
                    "ntuple_filters": "off [fixed]",
                    "tx_gre_csum_segmentation": "off [fixed]",
                    "tx_nocache_copy": "off [fixed]",
                    "tx_mpls_segmentation": "off [fixed]",
                    "tx_udp_tnl_csum_segmentation": "off [fixed]",
                    "udp_fragmentation_offload": "on",
                    "tx_sctp_segmentation": "on",
                    "tx_sit_segmentation": "off [fixed]",
                    "tx_checksum_fcoe_crc": "off [fixed]",
                    "hw_tc_offload": "off [fixed]",
                    "tx_checksum_ip_generic": "on [fixed]",
                    "tx_fcoe_segmentation": "off [fixed]",
                    "rx_vlan_filter": "off [fixed]",
                    "tx_vlan_offload": "off [fixed]",
                    "receive_hashing": "off [fixed]",
                    "tx_gre_segmentation": "off [fixed]"
                },
                "hw_timestamp_filters": [],
                "mtu": 65536,
                "device": "lo",
                "promisc": false,
                "timestamping": [
                    "rx_software",
                    "software"
                ],
                "ipv4": {
                    "broadcast": "host",
                    "netmask": "255.0.0.0",
                    "network": "127.0.0.0",
                    "address": "127.0.0.1"
                },
                "active": true,
                "type": "loopback"
            },
            "ansible_memtotal_mb": 992,
            "ansible_ssh_host_key_ecdsa_public": "AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBCXjbIZSZL8/kZ9MmVHbECF82mkMJj/YqxUhcgFiMBDqReK05235B4wUrQBXi3RmK/IE/i+d8lRjUcIRufV9XCA=",
            "ansible_device_links": {
                "masters": {},
                "labels": {},
                "ids": {
                    "sr0": [
                        "ata-QEMU_DVD-ROM_QM00003"
                    ]
                },
                "uuids": {
                    "vda1": [
                        "80b9b662-0a1d-4e84-b07b-c1bf19e72d97"
                    ]
                }
            },
            "ansible_default_ipv4": {
                "macaddress": "00:16:3e:2e:25:f9",
                "network": "172.17.48.0",
                "mtu": 1500,
                "broadcast": "172.17.63.255",
                "alias": "eth0",
                "netmask": "255.255.240.0",
                "address": "172.17.61.91",
                "interface": "eth0",
                "type": "ether",
                "gateway": "172.17.63.253"
            },
            "ansible_swapfree_mb": 0,
            "ansible_default_ipv6": {},
            "ansible_distribution_release": "Core",
            "ansible_system_vendor": "Alibaba Cloud",
            "ansible_apparmor": {
                "status": "disabled"
            },
            "ansible_cmdline": {
                "LANG": "zh_CN.UTF-8",
                "BOOT_IMAGE": "/boot/vmlinuz-3.10.0-693.11.6.el7.x86_64",
                "quiet": true,
                "rhgb": true,
                "crashkernel": "auto",
                "ro": true,
                "root": "UUID=80b9b662-0a1d-4e84-b07b-c1bf19e72d97"
            },
            "ansible_effective_user_id": 1000,
            "ansible_user_gid": 1000,
            "ansible_selinux": {
                "status": "disabled"
            },
            "ansible_product_version": "pc-i440fx-2.1",
            "ansible_os_family": "RedHat",
            "ansible_userspace_architecture": "x86_64",
            "ansible_product_uuid": "NA",
            "ansible_system": "Linux",
            "ansible_pkg_mgr": "yum",
            "ansible_memfree_mb": 230,
            "ansible_devices": {
                "vda": {
                    "scheduler_mode": "",
                    "rotational": "1",
                    "vendor": "0x1af4",
                    "sectors": "83886080",
                    "links": {
                        "masters": [],
                        "labels": [],
                        "ids": [],
                        "uuids": []
                    },
                    "sas_device_handle": null,
                    "sas_address": null,
                    "virtual": 1,
                    "host": "SCSI storage controller: Red Hat, Inc Virtio block device",
                    "sectorsize": "512",
                    "removable": "0",
                    "support_discard": "0",
                    "model": null,
                    "partitions": {
                        "vda1": {
                            "sectorsize": 512,
                            "uuid": "80b9b662-0a1d-4e84-b07b-c1bf19e72d97",
                            "links": {
                                "masters": [],
                                "labels": [],
                                "ids": [],
                                "uuids": [
                                    "80b9b662-0a1d-4e84-b07b-c1bf19e72d97"
                                ]
                            },
                            "sectors": "83884032",
                            "start": "2048",
                            "holders": [],
                            "size": "40.00 GB"
                        }
                    },
                    "holders": [],
                    "size": "40.00 GB"
                },
                "sr0": {
                    "scheduler_mode": "cfq",
                    "rotational": "1",
                    "vendor": "QEMU",
                    "sectors": "2097151",
                    "links": {
                        "masters": [],
                        "labels": [],
                        "ids": [
                            "ata-QEMU_DVD-ROM_QM00003"
                        ],
                        "uuids": []
                    },
                    "sas_device_handle": null,
                    "sas_address": null,
                    "virtual": 1,
                    "host": "IDE interface: Intel Corporation 82371SB PIIX3 IDE [Natoma/Triton II]",
                    "sectorsize": "512",
                    "removable": "1",
                    "support_discard": "0",
                    "model": "QEMU DVD-ROM",
                    "partitions": {},
                    "holders": [],
                    "size": "1024.00 MB"
                }
            },
            "ansible_user_uid": 1000,
            "ansible_memory_mb": {
                "real": {
                    "total": 992,
                    "used": 762,
                    "free": 230
                },
                "swap": {
                    "cached": 0,
                    "total": 0,
                    "free": 0,
                    "used": 0
                },
                "nocache": {
                    "used": 218,
                    "free": 774
                }
            },
            "ansible_distribution": "CentOS",
            "ansible_user_dir": "/home/rocky",
            "ansible_dns": {
                "nameservers": [
                    "100.100.2.136",
                    "100.100.2.138"
                ],
                "options": {
                    "attempts": "3",
                    "rotate": true,
                    "timeout": "2",
                    "single-request-reopen": true
                }
            },
            "ansible_distribution_major_version": "7",
            "module_setup": true,
            "ansible_processor_count": 1,
            "ansible_hostname": "victor",
            "ansible_processor_vcpus": 1,
            "ansible_swaptotal_mb": 0,
            "ansible_lsb": {},
            "ansible_real_group_id": 1000,
            "ansible_bios_date": "04/01/2014",
            "ansible_all_ipv6_addresses": [],
            "ansible_interfaces": [
                "lo",
                "eth0"
            ],
            "ansible_uptime_seconds": 4466108,
            "ansible_machine_id": "7d26c16f128042a684ea474c9e2c240f",
            "ansible_kernel": "3.10.0-693.11.6.el7.x86_64",
            "ansible_user_gecos": "",
            "ansible_system_capabilities_enforced": "True",
            "ansible_python": {
                "executable": "/usr/bin/python",
                "version": {
                    "micro": 5,
                    "major": 2,
                    "releaselevel": "final",
                    "serial": 0,
                    "minor": 7
                },
                "type": "CPython",
                "has_sslcontext": true,
                "version_info": [
                    2,
                    7,
                    5,
                    "final",
                    0
                ]
            },
            "ansible_processor_threads_per_core": 1,
            "ansible_fqdn": "iZ2ze4dhkm7u57j9fq08msZ",
            "ansible_mounts": [
                {
                    "block_used": 3361965,
                    "uuid": "80b9b662-0a1d-4e84-b07b-c1bf19e72d97",
                    "size_total": 42140499968,
                    "block_total": 10288208,
                    "mount": "/",
                    "block_available": 6926243,
                    "size_available": 28369891328,
                    "fstype": "ext4",
                    "inode_total": 2621440,
                    "options": "rw,relatime,data=ordered",
                    "device": "/dev/vda1",
                    "inode_used": 258829,
                    "block_size": 4096,
                    "inode_available": 2362611
                }
            ],
            "ansible_eth0": {
                "macaddress": "00:16:3e:2e:25:f9",
                "features": {
                    "tx_checksum_ipv4": "off [fixed]",
                    "generic_receive_offload": "on",
                    "tx_checksum_ipv6": "off [fixed]",
                    "tx_scatter_gather_fraglist": "off [fixed]",
                    "rx_all": "off [fixed]",
                    "highdma": "on [fixed]",
                    "rx_fcs": "off [fixed]",
                    "tx_lockless": "off [fixed]",
                    "tx_tcp_ecn_segmentation": "off [fixed]",
                    "tx_tcp6_segmentation": "on",
                    "tx_gso_robust": "off [fixed]",
                    "tx_ipip_segmentation": "off [fixed]",
                    "tx_tcp_mangleid_segmentation": "off",
                    "tx_checksumming": "on",
                    "vlan_challenged": "off [fixed]",
                    "loopback": "off [fixed]",
                    "fcoe_mtu": "off [fixed]",
                    "scatter_gather": "on",
                    "tx_checksum_sctp": "off [fixed]",
                    "tx_vlan_stag_hw_insert": "off [fixed]",
                    "rx_vlan_stag_hw_parse": "off [fixed]",
                    "tx_gso_partial": "off [fixed]",
                    "rx_vlan_stag_filter": "off [fixed]",
                    "large_receive_offload": "off [fixed]",
                    "tx_scatter_gather": "on",
                    "rx_checksumming": "on [fixed]",
                    "tx_tcp_segmentation": "on",
                    "netns_local": "off [fixed]",
                    "busy_poll": "off [fixed]",
                    "generic_segmentation_offload": "on",
                    "tx_udp_tnl_segmentation": "off [fixed]",
                    "tcp_segmentation_offload": "on",
                    "l2_fwd_offload": "off [fixed]",
                    "rx_vlan_offload": "off [fixed]",
                    "ntuple_filters": "off [fixed]",
                    "tx_gre_csum_segmentation": "off [fixed]",
                    "tx_nocache_copy": "off",
                    "tx_mpls_segmentation": "off [fixed]",
                    "tx_udp_tnl_csum_segmentation": "off [fixed]",
                    "udp_fragmentation_offload": "off [fixed]",
                    "tx_sctp_segmentation": "off [fixed]",
                    "tx_sit_segmentation": "off [fixed]",
                    "tx_checksum_fcoe_crc": "off [fixed]",
                    "hw_tc_offload": "off [fixed]",
                    "tx_checksum_ip_generic": "on",
                    "tx_fcoe_segmentation": "off [fixed]",
                    "rx_vlan_filter": "off [fixed]",
                    "tx_vlan_offload": "off [fixed]",
                    "receive_hashing": "off [fixed]",
                    "tx_gre_segmentation": "off [fixed]"
                },
                "pciid": "virtio0",
                "module": "virtio_net",
                "mtu": 1500,
                "device": "eth0",
                "promisc": false,
                "timestamping": [
                    "rx_software",
                    "software"
                ],
                "ipv4": {
                    "broadcast": "172.17.63.255",
                    "netmask": "255.255.240.0",
                    "network": "172.17.48.0",
                    "address": "172.17.61.91"
                },
                "active": true,
                "type": "ether",
                "hw_timestamp_filters": []
            },
            "ansible_nodename": "victor",
            "ansible_product_name": "Alibaba Cloud ECS",
            "ansible_machine": "x86_64",
            "ansible_system_capabilities": [
                ""
            ],
            "ansible_all_ipv4_addresses": [
                "172.17.61.91"
            ],
            "ansible_python_version": "2.7.5"
        }
    },
    "failed": {},
    "unreachable": {
        "192.168.1.1": {
            "unreachable": true,
            "msg": "Failed to connect to the host via ssh: ssh: connect to host 192.168.1.1 port 22: Connection refused\r\n",
            "changed": false
        }
    },
    "skipped": {}
}
```