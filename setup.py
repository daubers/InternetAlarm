from setuptools import setup

setup(
    name='InternetAlarm',
    version='0.1',
    packages=[''],
    url='',
    license='',
    author='matt',
    author_email='',
    description='',
    install_requires=[
        'pygame',
    ],
    dependency_links=[
        "https://github.com/daubers/pyping/tarball/master#egg=pyping-1.3",
    ],
    entry_points={
        'console_scripts': ['internet-alarm=internetalarm:main'],
    }
)
