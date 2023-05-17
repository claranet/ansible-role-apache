#!/usr/bin/env python


def test_https_listening(host):
    assert host.socket("tcp://0.0.0.0:443").is_listening

def test_ssl_certificates(host):
    command = "echo | openssl s_client -connect localhost:443"
    assert 'CN = localhost' in host.run(command).stdout
