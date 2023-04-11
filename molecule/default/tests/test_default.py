#!/usr/bin/env python

def test_http_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening
