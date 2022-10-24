# -*- coding: utf-8 -*-
#
# (C) Copyright IBM 2022.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Quantum-styles

Quantum styles for Matplotlib
"""
import os
import setuptools
import shutil
import matplotlib

MAJOR = 0
MINOR = 1
MICRO = 0

VERSION = '%d.%d.%d' % (MAJOR, MINOR, MICRO)

REQUIREMENTS = ['matplotlib>=3.3',
               ]

PACKAGES = setuptools.find_namespace_packages()
PACKAGE_DATA = {
}

DOCLINES = __doc__.split('\n')
DESCRIPTION = DOCLINES[0]
LONG_DESCRIPTION = "\n".join(DOCLINES[2:])


setuptools.setup(
    name='quantum-styles',
    version=VERSION,
    packages=PACKAGES,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url="",
    author="Paul Nation",
    author_email="paul.nation@ibm.com",
    license="Apache 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
    ],
    install_requires=REQUIREMENTS,
    zip_safe=False
)

# Inject mpl style files into correct location
mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
if not os.path.exists(mpl_stylelib_dir):
    os.makedirs(mpl_stylelib_dir)

parent_dir = os.path.dirname(__file__)
styles_dir = os.path.join(parent_dir, "mpl_styles")

for item in os.listdir(styles_dir):
    item_path = os.path.join(styles_dir, item)
    if os.path.isfile(item_path):
        shutil.copy(item_path, os.path.join(mpl_stylelib_dir, item))
        print('Copied {} to {}'.format(item, mpl_stylelib_dir))

# Inject Qiskit config files into correct location
qiskit_dir = os.path.join(os.path.expanduser("~"), ".qiskit")
if not os.path.exists(qiskit_dir):
    os.makedirs(qiskit_dir)

qiskit_styles_dir = os.path.join(parent_dir, "qiskit_styles")
for item in os.listdir(qiskit_styles_dir):
    item_path = os.path.join(qiskit_styles_dir, item)
    if os.path.isfile(item_path):
        shutil.copy(item_path, os.path.join(qiskit_dir, item))
        print('Copied {} to {}'.format(item, qiskit_dir))
