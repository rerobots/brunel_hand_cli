brunel_hand_cli
===============

Introduction
------------

This repository provides a command-line interface and Python package for the
`Brunel Hand <https://www.openbionics.com/shop/brunel-hand>`_
by `Open Bionics <https://www.openbionics.com>`_.

The main design goal is to provide a fast and reliable interface to the
firmware, `Beetroot <https://github.com/Open-Bionics/Beetroot>`_.  Motivating
use-cases are rapid prototyping and integration into more complicated
applications.


Development
-----------

To install the current release, try::

    pip install bhand

which uses `pip <https://pip.pypa.io/en/stable/>`_ to install dependencies and
this Python package. Now, connect the USB cable from your Brunel Hand into your
host machine, and try::

    bhand

It should print diagnostics data, e.g., the CPU temperature.  Note that serial
communications use `pySerial <http://pyserial.readthedocs.io/en/stable/>`_. To
obtain a help message, try::

    bhand --raw ?

The ``?`` command is recognized by the firmware Beetroot V1.01. (In some shells,
``?`` is a special character and has to be escaped. If the above fails, try
instead ``bhand --raw \?``.)

Current testing status for ``master`` branch: |build-status| (for details, visit
`the page on Travis CI <https://travis-ci.org/rerobots/brunel_hand_cli>`_).

.. |build-status| image:: https://travis-ci.org/rerobots/brunel_hand_cli.svg?branch=master


Bug reports and feature requests can be submitted in the issue tracker at
https://github.com/rerobots/brunel_hand_cli/issues


License
-------

This is free software, released under the Apache License, Version 2.0.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
