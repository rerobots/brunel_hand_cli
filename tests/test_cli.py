"""Basic tests of the command-line interface (CLI)

SCL <scott@rerobots.net>
Copyright (c) 2017, 2018 rerobots, Inc.
"""
try:
    from cStringIO import StringIO
except ImportError:  # if Python 3
    from io import StringIO
import sys

import bhand
from bhand import cli


def test_loopback_diagnostics():
    assert cli.main(['--loopback', '--raw', '#']) == 0

def test_version():
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    cli.main(['--version'])
    res = sys.stdout.getvalue().strip()
    sys.stdout = original_stdout
    assert bhand.__version__ == res
