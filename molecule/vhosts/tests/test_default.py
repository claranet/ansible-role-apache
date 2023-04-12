#!/usr/bin/env python

def test_apache_mod_status(host):
    command = """curl --head http://127.0.0.1/server-status"""
    cmd = host.run(command)
    assert '200 OK' in cmd.stdout

def test_apache_vhost_ssl_auth_fpm(host):
    command = """curl \
        --insecure --header "Host: molecule-fpm.oxalide-test.com" \
        https://127.0.0.1/var.php \
        --basic --user molecule-fpm-user:molecule-fpm-pass"""
    cmd = host.run(command)
    assert 'MYVAR: myvalue' in cmd.stdout
    assert 'MY2VAR: myvalue' in cmd.stdout