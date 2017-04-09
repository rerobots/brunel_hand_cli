#!/usr/bin/env python
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
"""Command-line interface for the Brunel Hand
"""
from __future__ import print_function
import argparse
import sys
import time

import serial


class BrunelHandSerial(object):
    def __init__(self, dev='/dev/ttyACM0'):
        self.ser = serial.Serial(dev, baudrate=115200, exclusive=True)

    def close(self):
        self.ser.close()

    def get_diagnostics_summary(self):
        if self.ser.in_waiting > 0:
            self.ser.reset_input_buffer()
        self.ser.write(b'#\n')
        time.sleep(0.1)
        return self.ser.read(self.ser.in_waiting).decode()

    def get_firmware_version(self):
        ds = self.get_diagnostics_summary()
        fw_index = ds.find('FW:')
        if fw_index < 0:
            return 'UNKNOWN'
        fw_v_text_end = ds[fw_index:].find('\n')
        if fw_v_text_end < 0:
            fw_v_text = ds[fw_index:]
        else:
            fw_v_text = ds[fw_index:(fw_index+fw_v_text_end)]
        return fw_v_text[3:].strip()

    def get_help(self):
        if self.ser.in_waiting > 0:
            self.ser.reset_input_buffer()
        self.ser.write(b'?\n')
        time.sleep(0.1)
        return self.ser.read(self.ser.in_waiting).decode()

    def send_text(self, txt):
        self.ser.write(bytes(txt+'\n', encoding='utf-8'))
        time.sleep(0.1)
        return self.ser.read(self.ser.in_waiting).decode()


def main(argv=None):
    bhs = BrunelHandSerial()
    if len(sys.argv) > 1:
        txt = ' '.join(sys.argv[1:])
        print('Sending command: ', txt)
        print(bhs.send_text(txt))
    else:
        print('Printing diagnostics. (Try `?` for help.)')
        print(bhs.get_diagnostics_summary())
    bhs.close()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
