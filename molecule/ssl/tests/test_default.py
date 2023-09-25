#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth

def get_ip_address(host):
    return host.interface("eth0").addresses[0]


def test_https_listening(host):
    assert host.socket("tcp://0.0.0.0:443").is_listening


def test_apache_vhost_ssl_auth_fpm(host):
    request = requests.get(
        url=f"https://{get_ip_address(host)}",
        headers={'Host': 'localhost'},
        verify=False
    )

    assert request.status_code == 403 or request.status_code == 200
