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
from setuptools import setup


setup(name='bhand',
      version='0.0.1',
      author='Scott C. Livingston',
      url='https://github.com/rerobots/brunel_hand_cli',
      description='command-line interface and Python package for the Brunel Hand by Open Bionics',
      classifiers=['License :: OSI Approved :: Apache Software License',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5'],
      packages=['bhand'],
      install_requires=['future', 'pyserial'],
      entry_points={'console_scripts': ['bhand = bhand.cli:main']}
      )
