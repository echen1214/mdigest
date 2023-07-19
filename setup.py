from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Best practices made easy for analysis of correlated motions from molecular dynamics simulations.'
LONG_DESCRIPTION = 'MDiGest is a best-practices-made-easy Python package that handles the most common issues in ' \
                   'the network-based analysis of correlated motions from molecular dynamics simulations.'

setup(
    name="mdigest",
    version=VERSION,
    author="Federica Maschietto, Brandon Allen",
    author_email="<federica.maschietto@gmail.com>, <brandon.allen@yale.edu>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy<=1.24.3',
                      'numba==0.56.4',
                      'python-louvain==0.15',
                      'pymol-open-source',
                      'pandas', 'seaborn',
                      'mdtraj', 'pyemma',
                      'MDAnalysis', 'silx',
                      'nglview', 'networkx'],
    # 'pandas>=1.5.3',
    # 'seaborn>=0.12.2',
    # 'mdtraj>=1.9.7',
    # 'pyemma==2.5.12',
    # 'MDAnalysis>=2.3.0',
    # 'silx>=1.1.1',
    # 'numba>=0.56.4',
    # 'python-louvain==0.15',
    # 'nglview>=3.0.3',
    # 'networkx>=2.6.3',
    # 'silx>=1.1'],
    keywords=[
        'python',
        'correlation',
        'molecular dynamics',
        'MD trajectory analysis',
        'correlated motions',
        'network analysis',
        'community network'
    ],
    url="https://github.com/fmaschietto/MDiGest",
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
)
