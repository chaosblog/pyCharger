from distutils.core import setup

setup(
    name='pyCharger',
    version='0.1dev',
    author='Chaosblog',
    author_email='chaosblog@quantentunnel.de',
    packages=['charger','charger.accucel6'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Turnigy Accucel-6 battery charger interface',
    install_requires=[
        "pyserial >= 2.5",
    ],
)
