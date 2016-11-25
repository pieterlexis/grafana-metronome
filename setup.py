import os
from setuptools import setup, find_packages
from pip.req import parse_requirements
import glob


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Parse requirements.txt
install_reqs = [str(ir.req) for ir in parse_requirements('./requirements.txt',
                                                         session=False)]

dashboardfiles = glob.glob('dashboards/*')

setup(
    name="metronome-graphite-finder",
    version="0.0.1.4",
    author="PowerDNS.COM BV",
    author_email="powerdns.support@powerdns.com",
    description=("Metronome finder for graphite-api"),
    license="GPLv2",
    keywords="PowerDNS Metronome Graphite",
    url="https://github.com/PowerDNS/grafana-metronome",
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_reqs,
    long_description=read('README.md'),
    data_files=[
        ('share/doc/metronome-graphite-finder/dashboards', dashboardfiles),
        ('share/doc/metronome-graphite-finder/example-configs', ['graphite-api/graphite-api.yaml', 'graphite-api/nginx.conf']),
        ],
    classifiers=[],
)
