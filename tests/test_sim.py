"""Basic tests of the simulated Brunel Hand

SCL <scott@rerobots.net>
Copyright (c) 2017 rerobots, Inc.
"""
from bhand import sim


def test_reset_input_buffer():
    dev = sim.Echo()
    dev.reset_input_buffer()
    assert dev.in_waiting == 0

def test_Echo_truncate():
    dev = sim.Echo(truncate=18)
    dev.write(b'f00f')
    assert len(dev.msg) == len('f00f')
    dev.write(b'#'*20)
    assert len(dev.msg) == 18
