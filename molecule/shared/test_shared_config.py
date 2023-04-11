#!/usr/bin/python3
import os
# Shared tests for all scenario

def get_apache_package_name(host):
    package_name = ""
    os_release = host.file('/etc/os-release')
    for os in ('centos', 'fedora', 'rhel','amzn'):
        if os_release.contains(f'ID="{os}"'):
            package_name = "httpd"
            break
        else:
            package_name = "apache2"

    return package_name

def test_apache_logrotate_run(host):
    package_name = get_apache_package_name(host)
    command = f"curl -k http://localhost && logrotate -f /etc/logrotate.d/{package_name}"
    cmd = host.run(command)
    log_file = host.file(f"/var/log/{package_name}/vhosts/default/access.log.1.gz")
    assert log_file.exists
    assert cmd.rc == 0

def test_apache_mpm_prefork(host):
    package_name = get_apache_package_name(host)
    apache_get_mpm = "httpd -V | grep 'Server MPM'" if package_name == "httpd" else "a2query -M"
    output = host.check_output(f"{apache_get_mpm}")
    assert "prefork" in output
