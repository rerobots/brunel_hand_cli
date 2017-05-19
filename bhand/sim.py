# Copyright (C) 2017 rerobots, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Simulation and mock capabilities
"""
import copy
import sys

from . import __version__ as bhand_pkg_version


class BaseHandSim(object):
    pass


class Echo(BaseHandSim):
    def __init__(self, outfile=None, truncate=256):
        """Instantiate the "echo" mock

        `outfile` is a file-like object to which received serial input
        should be echoed, or if it is None (the default case), then
        use stdout.

        `truncate` is the maximum length of accepted input strings,
        e.g., as given to the method write().
        """
        if outfile is None:
            self.logging = sys.stdout
        else:
            self.logging = outfile
        self.truncate_len = truncate
        self.in_waiting = 0


    def read(self, count=1):
        self.logging.write('ECHO: read({!r})\n'.format(count))
        if self.msg == '#':
            self.msg = ''
            try:
                res = b'FW: Echo(BaseHandSim) V'+bytes(bhand_pkg_version, encoding='utf-8')
            except TypeError:  # Try instead to use Python 2 `bytes`?
                res = b'FW: Echo(BaseHandSim) V'+bytes(bhand_pkg_version)
        else:
            return b''

    def write(self, msg):
        self.logging.write('ECHO: write({!r})\n'.format(msg))
        if len(msg) > self.truncate_len:
            msg = msg[:self.truncate_len]
        self.msg = copy.copy(msg.decode())

    def reset_input_buffer(self):
        self.in_waiting = 0

    def close(self):
        return
