# !/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Ayumu Saito
# SPDX-License-Identifier: BSD-3-Clause

import os
from glob import glob
from setuptools import find_packages,  setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/'+ package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch/launch.'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ayumu Saito',
    maintainer_email='saito.ayumu1002@icloud.com',
    description='ROS 2 sample: /countup talker & listener (std_msgs/Int16).',
    license='GPL-3.0-only',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
        ],
    },
)icense='GPL-3.0-only',
