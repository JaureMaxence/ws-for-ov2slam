from setuptools import find_packages, setup

package_name = 'controller_launcher'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/controller_launcher']),
        ('share/controller_launcher', ['package.xml']),
        ('share/controller_launcher/launch', ['launch/controller_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='imr',
    maintainer_email='abdulahm@fel.cvut.cz',
    description='Launch controller and robot nodes',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
