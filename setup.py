from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],  # 直下に mypkg/ がある前提
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Ayumu Saito',
    maintainer_email='saito.ayumu1002@icloud.com',  # ← icoud→icloud に修正
    description='ROS 2 sample: talker/listener for /countup (Int16).',
    license='GPL-3.0-only',
    extras_require={
        'test': ['pytest'],
    },
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',
            'listener = mypkg.listener:main',
        ],
    },
)

