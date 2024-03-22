#!/usr/bin/python3
import requests

# Shared tests for all scenario


def get_apache_package_name(host):
    os_release = host.file("/etc/os-release")
    for os in ("centos", "fedora", "rhel", "amzn"):
        if os_release.contains(f'ID="{os}"'):
            return "httpd"

    return "apache2"


def test_apache_logrotate_run(host):
    package_name = get_apache_package_name(host)
    ip_address = host.interface("eth0").addresses[0]
    requests.get(
        url=f"http://{ip_address}",
        headers={"Host": "claranet.example.com"},
        verify=False,
    )

    command = host.run(f"logrotate -f /etc/logrotate.d/{package_name}")
    log_file_compressed = host.file(
        f"/var/log/{package_name}/vhosts/claranet.example.com/access.log.1.gz"
    )
    log_file = host.file(
        f"/var/log/{package_name}/vhosts/claranet.example.com/access.log.1"
    )

    assert log_file.exists or log_file_compressed.exists
    assert command.rc == 0


def test_apache_mpm_prefork(host):
    package_name = get_apache_package_name(host)
    apache_get_mpm = (
        "httpd -V | grep 'Server MPM'" if package_name == "httpd" else "a2query -M"
    )
    output = host.check_output(f"{apache_get_mpm}")

    assert "prefork" in output


def test_hardening(host):
    ip_address = host.interface("eth0").addresses[0]
    request = requests.get(url=f"https://{ip_address}", verify=False)

    assert request.headers["Server"] == "Apache"
