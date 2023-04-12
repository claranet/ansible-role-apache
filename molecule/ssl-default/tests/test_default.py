#!/usr/bin/env python

def test_https_listening(host):
    assert host.socket("tcp://0.0.0.0:443").is_listening
