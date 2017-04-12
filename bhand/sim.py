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
import sys


class BaseHandSim(object):
    pass


class Echo(BaseHandSim):
    def __init__(self, outfile=None):
        """Instantiate the "echo" mock

        `logging` is a file-like object to which received serial input
        should be echoed, or if it is None (the default case), then
        use stdout.
        """
        if outfile is None:
            self.logging = sys.stdout
        else:
            self.logging = outfile
        self.in_waiting = 0


    def read(self, count=1):
        return b''

    def write(self, msg):
        self.logging.write('ECHO: ' + msg.decode())
        return

    def reset_input_buffer(self):
        return

    def close(self):
        return
