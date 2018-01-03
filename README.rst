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


Participating
-------------

All participation must follow our code of conduct, elaborated in the file
CODE_OF_CONDUCT.md in the same directory as this README.

Reporting errors, requesting features
`````````````````````````````````````

Please first check for prior reports that are similar or related in the issue
tracker at https://github.com/rerobots/brunel_hand_cli/issues
If your observations are indeed new, please `open a new
issue <https://github.com/rerobots/brunel_hand_cli/issues/new>`_

Security disclosures are given the highest priority and should be sent to Scott
<scott@rerobots.net>, optionally encrypted using his `public key
<http://pgp.mit.edu/pks/lookup?op=get&search=0x79239591A03E2274>`_. Please do so
before opening a public issue to allow us an opportunity to find a fix.

Contributing changes or new code
````````````````````````````````

Contributions are welcome! There is no formal declaration of code style. Just
try to follow the style and structure currently in the repository.

Contributors, who are not rerobots employees, must agree to the `Developer
Certificate of Origin <https://developercertificate.org/>`_. Your agreement is
indicated explicitly in commits by adding a Signed-off-by line with your real
name. (This can be done automatically using ``git commit --signoff``.)


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
