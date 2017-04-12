import bhand.cli


def test_loopback_diagnostics():
    assert bhand.cli.main(['--loopback', '--raw', '#']) == 0
