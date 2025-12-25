#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

from glob import glob
import os
from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/mypkg']),
        ('share/mypkg', ['package.xml']),
        ('share/mypkg/launch', glob('launch/*.launch.py')),
    ]
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='...',
    maintainer_email='...',
    description='...',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
        ],
    },
)
