#!/usr/bin/env python
import requests
from requests.auth import HTTPBasicAuth


def get_ip_address(host):
    return host.interface("eth0").addresses[0]


def test_apache_mod_status(host):
    request = requests.head(
        url=f"https://{get_ip_address(host)}/server-status", verify=False
    )

    assert request.status_code == 403 or request.status_code == 200


def test_apache_vhost_auth_fpm(host):
    request = requests.get(
        url=f"http://{get_ip_address(host)}/var.php",
        headers={"Host": "claranet.example.com"},
        auth=HTTPBasicAuth("molecule-user", "molecule-pass"),
        verify=False,
    )

    assert "MYVAR: myvalue" in request.text
    assert "MY2VAR: myvalue" in request.text
    assert 200 == request.status_code


def test_apache_letsencrypt_challenge(host):
    request = requests.get(
        url=f"https://{get_ip_address(host)}/.well-known/acme-challenge/challenge.html",
        headers={"Host": "certbot.example.com"},
        auth=HTTPBasicAuth("molecule-fpm-user", "molecule-fpm-pass"),
        verify=False,
    )

    assert "This is a letsencrypt challenge" in request.text
    assert 200 == request.status_code
