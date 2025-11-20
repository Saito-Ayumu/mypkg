from setuptools import setup

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],  # mypkg/ フォルダをPythonパッケージとして扱う
    data_files=[
        ('share/ament_index/resource_index/packages', [f'resource/{package_name}']),
        (f'share/{package_name}', ['package.xml']),
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
)

