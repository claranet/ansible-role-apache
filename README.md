# Ansible role - apache
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-apache?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-apache?style=flat-square)](https://github.com/claranet/ansible-role-apache/releases)
[![Status](https://img.shields.io/github/actions/workflow/status/claranet/ansible-role-apache/molecule.yml?branch=main&label=tests&style=flat-square)](https://github.com/claranet/ansible-role-apache/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/apache)


> :star: Star us on GitHub — it motivates us a lot!

Install and configure Apache 2

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.apache
```

## :gear: Role variables

Variable                                    | Default value                              | Description
--------------------------------------------|--------------------------------------------|-----------------------------------------------------------------------------------
apache_additionnal_packages                 | **[]**                                     | Additionnal packages to install with apache packages       
apache_service_enabled                      | **true**                                   | Enable apache systemd service       
apache_service_state                        | **started**                                | Systemd service state
apache_ports                                | **[80]**                                   | Listen ports for HTTP       
apache_ssl_ports                            | **[443]**                                  | Listen ports for SSL       
apache_gnutls_ports                         | **[443]**                                  | Listen ports for GnuTLS
apache_mods                                 | **{}**                                     | Module to enable or to disable, example: {ssl:present, lua:present}
apache_conf                                 | **{}**                                     | Configurations to enable or disable. Only available for debian family       
apache_mpm                                  | **prefork**                                | Module for multiprocessus to use       
apache_prefork_server_limit                 | **25**                                     | Server limit for prefork module       
apache_prefork_start_servers                | **5**                                      | Start servers for prefork module      
apache_prefork_min_spare_servers            | **5**                                      | Min Spare servers for prefork module       
apache_prefork_max_spare_servers            | **10**                                     | Max Spare servers for prefork module
apache_prefork_max_request_workers          | **256**                                    | Max request workers for prefork module
apache_prefork_max_connections_per_child    | **10000**                                  | Max connections per child for prefork module
apache_worker_server_limit                  | **16**                                     | Server limit for worker module        
apache_worker_start_servers                 | **3**                                      | Start servers for worker module       
apache_worker_min_spare_threads             | **75**                                     | Min Spare threads for worker module       
apache_worker_max_spare_threads             | **250**                                    | Max Spare threads for worker module
apache_worker_thread_limit                  | **64**                                     | Threads limit for worker module
apache_worker_threads_per_child             | **25**                                     | Threads per child for worker module
apache_worker_max_connections_per_child     | **10000**                                  | Max connections per child for worker module
apache_worker_max_clients                   | **400**                                    | Max clients for worker module
apache_event_server_limit                   | **16**                                     | Server limit for event module        
apache_event_start_servers                  | **3**                                      | Start servers for event module       
apache_event_min_spare_threads              | **75**                                     | Min Spare threads for event module       
apache_event_max_spare_threads              | **250**                                    | Max Spare threads for event module
apache_event_thread_limit                   | **64**                                     | Threads limit for event module
apache_event_threads_per_child              | **25**                                     | Threads per child for event module
apache_event_max_connections_per_child      | **10000**                                  | Max connections per child for event module
apache_event_max_clients                    | **400**                                    | Max clients for event module
apache_remoteip                             | **false**                                  | Enable remoteip config
apache_remoteip_header                      | **X-Forwarded-For**                        | Remote ip header
apache_remoteip_proxies                     | **[127.0.0.1]**                            | Remote ip proxies
apache_ssl_protocol                         | **-SSLv2 -SSLv3 -TLSv1 -TLSv1.1**          | SSL Protocol
apache_ssl_ciphersuite                      | **autogenerated value**                    | SSL cipher suite
apache_ssl_honorcipherorder                 | **on**                                     | SSL honorcipherorder
apache_ssl_compression                      | **off**                                    | SSL compression
apache_ssl_usestapling                      | **off**                                    | SSL use stapling
apache_ssl_staplingcache                    | **off**                                    | SSL stapling cache
apache_ssl_staplingrespondertimeout         | **5**                                      | SSL stapling responder timeout
apache_ssl_staplingreturnrespondererrors    | **off**                                    | SSL stapling return responders errors
apache_ssl_sessioncache                     | **512000**                                 | SSL session cache
apache_ssl_sessioncachetimeout              | **300**                                    | SSL session cache timeout
apache_server_tokens                        | **Prod**                                   | Server tokens
apache_server_signature                     | **Off**                                    | Server signature
apache_trace_enable                         | **off**                                    | Enable trace for service
apache_hostname_lookups                     | **"Off"**                                  | Hostname lookups for manage performance
apache_listen_backlog                       | **1024**                                   | Listen backlog
apache_default_vhost_ssl                    | **false**                                  | Path to certificate for default virtual host
apache_default_vhost_crt                    | **""**                                     | Path to certificate for default virtual host
apache_default_vhost_key                    | **""**                                     | Path to certificate key for default virtual host
apache_default_vhost_ssl_certs_path         | **"/etc/{{ _apache_package_name }}/ssl"**  | Path to certificates for default virtual hosts. Used only when apache_default_vhost_crt and apache_default_vhost_key are empty
apache_default_vhost_ip                     | **"*"**                                    |  Listen address for default virtual host
apache_default_vhost_http_port              | **80**                                     | HTTP port for default virtual host
apache_default_vhost_ssl_http_port          | **443**                                    | HTTPS port for default virtual host
apache_vhosts_user                          | **""**                                     | Default user owner for virtual hosts
apache_vhosts_group                         | **""**                                     | Default group owner for virtual hosts
apache_vhosts_directory                     | **"/srv/www"**                             | Directory for store virtual hosts files
apache_vhosts                               | **[]**                                     | Default user owner for default vhost
apache_vhosts_user                          | **""**                                     | Default user owner for default vhost
apache_vhosts_default                       | [See here](/defaults/main.yml#L124)        | Default vhost default options 
apache_vhosts                               | **[]**                                     | List of virtual hosts to config. [Example of configuration here](/molecule/vhosts/converge.yml#L12)
apache_certbot_webroot                      | **"/var/www/letsencrypt"**                 | Path to certbot letsencrypt certificates


## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

* default scenario: install and configure apache with default config(without ssl)
```yaml
---
- hosts: all
  roles:
    - claranet.apache
```

* ssl: install and configure apache with ssl for default virtual host
```yaml
---
- hosts: all
  vars:
    - apache_default_vhost_ssl: true
  roles:
    - claranet.apache
```
* virtual host: install and configure apache and add virtual host configuration
```yaml
---
- hosts: all
  vars:
    - apache_default_vhost_ssl: true
    - apache_vhosts:
        - name: molecule.oxalide-test.com
          state: present
          http: true
          create_docroot: true
          docroot: current
          auth:
            name: molecule
            file: molecule-file
            username: molecule-user
            password: molecule-pass
          custom_options:
            SetEnv:
              - "MYVAR myvalue"
              - "MY2VAR myvalue"
        - name: molecule-fpm.oxalide-test.com
          state: present
          https: true
          ssl:
            crt: "/etc/letsencrypt/live/molecule-fpm.oxalide-test.com/cert.pem"
            key: "/etc/letsencrypt/live/molecule-fpm.oxalide-test.com/privkey.pem"
          php_fpm: true
          php_fpm_status: true
          php_fpm_host: "proxy:unix:{{php_fpm_sock}}|fcgi://localhost/"
          create_docroot: true
          docroot: current
          auth:
            name: molecule-fpm
            file: molecule-fpm-file
            username: molecule-fpm-user
            password: molecule-fpm-pass
          custom_options:
            SetEnv:
              - "MYVAR myvalue"
              - "MY2VAR myvalue"
  roles:
    - claranet.apache
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

* SSL packages for enable apache ssl module are installed
* Set apache servers token config to **Prod** value
* Disabling apache server signature and apache trace token

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
