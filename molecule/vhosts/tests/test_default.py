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

def test_apache_letsencrypt_challenge(host):
    command = """curl \
        --header "Host: certbot.retail.oxalide-test.com" \
        http://127.0.0.1/.well-known/acme-challenge/challenge.html \
        --basic --user molecule-fpm-user:molecule-fpm-pass"""
    cmd = host.run(command)
    assert 'This is a letsencrypt challenge' in cmd.stdout
