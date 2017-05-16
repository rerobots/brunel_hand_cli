from bhand import sim


def test_reset_input_buffer():
    dev = sim.Echo()
    dev.reset_input_buffer()
    assert dev.in_waiting == 0
