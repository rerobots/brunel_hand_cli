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
from __future__ import absolute_import
from builtins import bytes

import argparse
import sys
import time

import serial

from . import sim


class BrunelHandSerial(object):
    def __init__(self, dev='/dev/ttyACM0'):
        """Instantiate wrapper of serial connection to Brunel Hand
        """
        if isinstance(dev, sim.BaseHandSim):
            self.ser = dev
        else:
            self.ser = serial.Serial(dev, baudrate=115200, exclusive=True)

    def close(self):
        self.ser.close()

    def get_diagnostics_summary(self):
        """Get diagnostics from firmware

        This is equivalent to send_text('#').
        """
        if self.ser.in_waiting > 0:
            self.ser.reset_input_buffer()
        self.ser.write(b'#\n')
        time.sleep(0.2)
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

    def get_mode(self):
        dsummary = self.get_diagnostics_summary()
        for k in dsummary.split('\n'):
            if k.startswith('Mode'):
                return k.split('\t')[1].strip()
        return None

    def get_csv_1line(self):
        mode = self.get_mode()
        if mode is None:
            raise ValueError('Firmware mode unknown')
        if mode != 'CSV':
            already_csv_mode = False
            self.send_text('A4')  # Assume Beetroot V1.01
        else:
            already_csv_mode = True
        blob = self.ser.read(self.ser.in_waiting).decode()
        while len(blob) < 60:
            blob += self.ser.read(self.ser.in_waiting).decode()
        if not already_csv_mode:
            self.send_text('A4')  # Assume Beetroot V1.01
        rfound = blob.rfind('\n')
        if rfound < 0:
            raise ValueError('Malformed CSV data')
        rrfound = blob[:(rfound-1)].rfind('\n')
        if rrfound < 0:
            raise ValueError('Malformed CSV data')
        return blob[(rrfound+1):rfound]

    def get_help(self):
        if self.ser.in_waiting > 0:
            self.ser.reset_input_buffer()
        self.ser.write(b'?\n')
        time.sleep(0.2)
        return self.ser.read(self.ser.in_waiting).decode()

    def send_text(self, txt):
        self.ser.write(bytes(txt+'\n', encoding='utf-8'))
        time.sleep(0.2)
        return self.ser.read(self.ser.in_waiting).decode()


def main(argv=None):
    aparser = argparse.ArgumentParser(description=('Command-line interface'
                                                   ' for the Brunel Hand'))
    aparser.add_argument('--loopback', action='store_true', default=False,
                         help='do not send anything; echo values that would be sent')
    aparser.add_argument('--raw', metavar='CMD', nargs='+',
                         help='raw commands to send directly',
                         dest='raw_command', action='store')
    aparser.add_argument('--fw-help', action='store_true', default=False,
                         help='print help message from firmware',
                         dest='fw_help')
    aparser.add_argument('--get-csv', action='store_true', default=False,
                         help='get finger pose data as one line of CSV',
                         dest='get_csv')
    argv_parsed = aparser.parse_args(argv)

    if argv_parsed.loopback:
        dev = sim.Echo()
    else:
        dev = '/dev/ttyACM0'

    bhs = BrunelHandSerial(dev)
    if argv_parsed.raw_command is not None:
        txt = ' '.join(argv_parsed.raw_command)
        print('Sending command: ', txt)
        print(bhs.send_text(txt))
    elif argv_parsed.fw_help:
        print(bhs.get_help())
    elif argv_parsed.get_csv:
        print(bhs.get_csv_1line())
    else:
        print('Printing diagnostics. (Try `-h` for help.)')
        print(bhs.get_diagnostics_summary())
    bhs.close()

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
