"""Basic tests of the command-line interface (CLI)

SCL <scott@rerobots.net>
Copyright (c) 2017, 2018 rerobots, Inc.
"""
import bhand.cli


def test_loopback_diagnostics():
    assert bhand.cli.main(['--loopback', '--raw', '#']) == 0
