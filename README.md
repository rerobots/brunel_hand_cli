# brunel_hand_cli

## Introduction

This repository provides a command-line interface and Python package for the
[Brunel Hand](https://www.openbionics.com/shop/brunel-hand)
by [Open Bionics](https://www.openbionics.com).

The main design goal is to provide a fast and reliable interface to the
firmware, [Beetroot](//github.com/Open-Bionics/Beetroot).  Motivating use-cases
are rapid prototyping and integration into more complicated applications.


## Development

Go to your clone of the repository, and try

    pip install .

which uses [pip](https://pip.pypa.io/en/stable/) to install dependencies and
installs this Python package. Now, connect the USB cable from your Brunel Hand
into your host machine, and try

    bhand

It should print diagnostics data, e.g., the CPU temperature.  Note that serial
communications use [pySerial](http://pyserial.readthedocs.io/en/stable/).


## License

This is free software, released under the Apache License, Version 2.0.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
