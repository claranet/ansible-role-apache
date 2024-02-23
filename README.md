# Ansible role - apache
[![Maintainer](https://img.shields.io/badge/maintained%20by-claranet-e00000?style=flat-square)](https://www.claranet.fr/)
[![License](https://img.shields.io/github/license/claranet/ansible-role-apache?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-apache?style=flat-square)](https://github.com/claranet/ansible-role-apache/releases)
[![Status](https://img.shields.io/github/actions/workflow/status/claranet/ansible-role-apache/molecule.yml?style=flat-square&label=tests&branch=main)](https://github.com/claranet/ansible-role-apache/actions?query=workflow%3A%22Ansible+Molecule%22)
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

| Variable                                    | Default value                              | Description                                                                                           |
| ------------------------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------------------------- |
| apache_additionnal_packages                 | []                                         | A list of additional packages to be installed                                                         |
| apache_service_enabled                      | true                                       | Whether the Apache service is enabled or not                                                          |
| apache_service_state                        | started                                    | The state of the Apache service, whether started, stopped, or restarted                               |
| apache_ports                                | [80]                                       | The ports on which HTTP requests are listened to                                                      |
| apache_ssl_ports                            | [443]                                      | The ports on which HTTPS requests are listened to                                                     |
| apache_gnutls_ports                         | [443]                                      | The ports on which GnuTLS encrypted requests are listened to                                          |
| [apache_mods](#apache_mods)                 | {}                                         | The modules to be loaded by Apache                                                                    |
| [apache_conf](#apache_conf)                 | {}                                         | Additional Apache configuration                                                                       |
| apache_mpm                                  | prefork                                    | The MPM (Multi-Processing Module) to be used with Apache                                              |
| apache_prefork_server_limit                 | 256                                        | The maximum number of child processes Apache can fork                                                 |
| apache_prefork_start_servers                | 5                                          | The number of child processes Apache will fork on startup                                             |
| apache_prefork_min_spare_servers            | 5                                          | The minimum number of idle child processes Apache will maintain                                       |
| apache_prefork_max_spare_servers            | 10                                         | The maximum number of idle child processes Apache will maintain                                       |
| apache_prefork_max_request_workers          | 256                                        | The maximum number of requests that can be processed by a child process                               |
| apache_prefork_max_connections_per_child    | 10000                                      | The maximum number of connections a child process can handle before it is terminated                  |
| apache_worker_server_limit                  | 16                                         | The maximum number of child processes Apache can fork (Worker MPM)                                    |
| apache_worker_start_servers                 | 3                                          | The number of child processes Apache will fork on startup (Worker MPM)                                |
| apache_worker_min_spare_threads             | 75                                         | The minimum number of idle threads Apache will maintain (Worker MPM)                                  |
| apache_worker_max_spare_threads             | 250                                        | The maximum number of idle threads Apache will maintain (Worker MPM)                                  |
| apache_worker_thread_limit                  | 64                                         | The maximum number of threads a child process can create (Worker MPM)                                 |
| apache_worker_threads_per_child             | 25                                         | The number of threads Apache will create for each child process (Worker MPM)                          |
| apache_worker_max_clients                   | 400                                        | The maximum number of simultaneous requests that can be handled by a child process (Worker MPM)       |
| apache_worker_max_connections_per_child     | 10000                                      | The maximum number of connections a child process can handle before it is terminated (Worker MPM)     |
| apache_event_server_limit                   | 16                                         | The maximum number of child processes Apache can fork (Event MPM)                                     |
| apache_event_start_servers                  | 3                                          | The number of child processes Apache will fork on startup (Event MPM)                                 |
| apache_event_min_spare_threads              | 75                                         | Min Spare threads for event module                                                                    |
| apache_event_max_spare_threads              | 250                                        | The maximum number of idle threads Apache will maintain (Event MPM)                                   |
| apache_event_thread_limit                   | 64                                         | The maximum number of threads a child process can create (Event MPM)                                  |
| apache_event_threads_per_child              | 25                                         | The number of threads Apache will create for each child process (Event MPM)                           |
| apache_event_max_clients                    | 400                                        | The maximum number of simultaneous requests that can be handled by a child process (Event MPM)        |
| apache_event_max_connections_per_child      | 10000                                      | The maximum number of connections a child process can handle before it is terminated (Event MPM)      |
| apache_remoteip                             | false                                      | Whether remote IP address information should be updated from the X-Forwarded-For header               |
| apache_remoteip_header                      | X-Forwarded-For                            | The name of the header containing the remote IP address                                               |
| apache_remoteip_proxies                     | [127.0.0.1]                                | A list of trusted proxy servers                                                                       |
| apache_ssl_protocol                         | -SSLv2 -SSLv3 -TLSv1 -TLSv1.1              | A list of SSL protocols that should be disabled                                                       |
| apache_ssl_ciphersuite                      | see the code                               | The ciphersuite configuration for HTTPS encryption                                                    |
| apache_ssl_honorcipherorder                 | on                                         | Whether to use the server's preferred ciphersuite order                                               |
| apache_ssl_compression                      | off                                        | Whether to compress SSL traffic                                                                       |
| apache_ssl_usestapling                      | on                                         | Whether to enable OCSP stapling for SSL certificate revocation checking                               |
| apache_ssl_staplingcache                    | 128000                                     | The size of the cache used for OCSP stapling                                                          |
| apache_ssl_staplingrespondertimeout         | 5                                          | SSL stapling responder timeout                                                                        |
| apache_ssl_staplingreturnrespondererrors    | off                                        | SSL stapling return responders errors                                                                 |
| apache_ssl_sessioncache                     | 512000                                     | SSL session cache                                                                                     |
| apache_ssl_sessioncachetimeout              | 300                                        | SSL session cache timeout                                                                             |
| apache_server_tokens                        | Prod                                       | Server tokens                                                                                         |
| apache_server_signature                     | Off                                        | Server signature                                                                                      |
| apache_trace_enable                         | off                                        | Enable trace for service                                                                              |
| apache_hostname_lookups                     | "Off"                                      | Hostname lookups for manage performance                                                               |
| apache_listen_backlog                       | 1024                                       | Listen backlog                                                                                        |
| apache_default_vhost_ssl                    | false                                      | Path to certificate for default virtual host                                                          |
| apache_default_vhost_crt                    | ""                                         | Path to certificate for default virtual host                                                          |
| apache_default_vhost_key                    | ""                                         | Path to certificate key for default virtual host                                                      |
| apache_default_vhost_ssl_certs_path         | "/etc/{{ _apache_package_name }}/ssl"      | Path to certificates for default virtual hosts. Used only when apache_default_vhost_crt and apache_default_vhost_key are empty |
| apache_default_vhost_ip                     | "*"                                        | Listen address for default virtual host                                                               |
| apache_default_vhost_http_port              | 80                                         | HTTP port for default virtual host                                                                    |
| apache_default_vhost_ssl_http_port          | 443                                        | HTTPS port for default virtual host                                                                   |
| apache_vhosts_user                          | ""                                         | Default user owner for virtual hosts                                                                  |
| apache_vhosts_group                         | ""                                         | Default group owner for virtual hosts                                                                 |
| apache_vhosts_directory                     | "/srv/www"                                 | Directory for store virtual hosts files                                                               |
| [apache_vhosts](#apache_vhosts)             | []                                         | Default user owner for default vhost                                                                  |
| apache_vhosts_user                          | ""                                         | Default user owner for default vhost                                                                  |
| apache_vhosts_default                       | [See here](/defaults/main.yml#L124)        | Common options to set by default to all vhosts                                                        |
| apache_certbot_webroot                      | "/var/www/letsencrypt"                     | Path to certbot letsencrypt certificates                                                              |


## Role Variable Attributes

### apache_mods

| Attribute           | Type     | Default Value                  | Description                                                                                                                   |
| --------------------|----------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| id                  | string   |   **required**                 | The domain name of the virtual host.                                                                                          |
| state               | string   |    absent or present           | The domain name aliases of the virtual host.                                                                                  |
| identifier          | string   |                                | The Identifier module.                                                                                                        |

&nbsp;

### apache_conf

| Attribute           | Type     | Default Value                  | Description                                                                                                                   |
| --------------------|----------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| id                  | string   |   **required**                 | Name of conf to enable or disable                                                                                             |
| state               | string   |    absent or present           | The state of conf (present for enable, absent for disable)                                                                    |

&nbsp;


### apache_vhosts

| Attribute           | Type     | Default Value                  | Description                                                                                                                   |
| --------------------|----------|--------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Name                | string   |   **required**                 | The domain name of the virtual host.                                                                                          |
| aliases             | list     |                                | The domain name aliases of the virtual host.                                                                                  |
| mailadmin           | string   |                                | The email address of the server administrator.                                                                                |
| proxy               | dict     |                                | The proxy configuration, by example: {path: /, url: ["http://localhost:6000/"], proxy_set: "lbmethod=bytraffic", proxy_requests: "Off", proxy_preverve_host: "On"}|
| state               | string   |   'present'                    | Whether the virtual host should be "present" or "absent".                                                                     |
| http                | boolean  |     true                       | Config http with default http port                                                                                            |
| https_redir         | boolean  |                                | Config http redirect to https                                                                                                 |
| https               | boolean  |                                | Config https with default https port                                                                                          |
| ip                  | string   |                                | The IP address to bind the virtual host to.                                                                                   |
| port                | int      |                                | The TCP port to bind the virtual host to.                                                                                     |
| php_fpm             | boolean  | true                           | Enable PHP-FPM for serving PHP scripts.                                                                                       |
| php_fpm_host        | string   | '127.0.0.1:9001'               | The IP address and port of the PHP-FPM server.                                                                                |
| php_fpm_status      | boolean  | true                           | Whether to enable the PHP-FPM server status page.                                                                             |
| add_webroot         | boolean  | true                           | Whether to create a webroot for the virtual host.                                                                             |
| create_docroot      | boolean  | true                           | Whether to create the document root directory.                                                                                |
| docroot             | string   | 'current'                      | The location of the virtual host's root directory.                                                                            |
| auth                | dict     |                                | Setup authentication, Define the username, password, and authentication file for the virtual host by example, {name: "test", username: "test", password: "test, file: "test-file"}         |
| ssl                 | dict     |                                | Define the paths to the SSL certificate files. By ex: {crt: "/etc/ssl/default", key: "/etc/ssl/key", 'chain': "/etc/ssl/chain"}. Only crt and key are required. Values can be path or cert content directly                      |
&nbsp;



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
    apache_default_vhost_ssl: true
    apache_vhosts:
      - name: molecule.example.com
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
      - name: molecule-fpm.example.com
        state: present
        https: true
        ssl:
          crt: "/etc/letsencrypt/live/molecule-fpm.example.com/cert.pem"
          key: "/etc/letsencrypt/live/molecule-fpm.example.com/privkey.pem"
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

      - name: mon.oxalide.org
        aliases:
          - oxalide.org
        mailadmin: noccy@oxalide.com
        state: absent
        http: true
        create_docroot: true
        docroot: current
        proxy:
          path: /
          url:
            - http://localhost:5050/
          proxy_set: "lbmethod=bytraffic"
  roles:
    - claranet.apache
```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
