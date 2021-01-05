.. image:: https://travis-ci.org/lukassup/python-cli.svg?branch=master
    :target: https://travis-ci.org/lukassup/python-cli

starships-of-war
========

``starships-of-war`` is a simple Python CLI CRUD application to rank starships by
Hyperdriver or Sublight speed.

.. _installation:

Installation
------------

Supported versions of Python are: 2.6, 2.7, 3.4, 3.5 and 3.6. The
recommended way to install this package is via `pip
<https://pypi.python.org/pypi/pip>`_.

python setup.py install

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ pip install ./starships-of-war

For instructions on installing python and pip see "The Hitchhiker's Guide to
Python" `Installation Guides
<http://docs.python-guide.org/en/latest/starting/installation/>`_.

Alternatively use ``easy_install``:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ easy_install ./starships-of-war

.. _usage:

Usage
-----

Rank the Startwars Ships easy: Choose for Hyperdrive or sublight speedy and compare.


.. code-block::

    $ starships-of-war ordered --help
    usage: starships-of-war ordered [-h] [-v]


    optional arguments:
    -h, --help            show help message and reload
    -v, --verbose         more verbose


.. _development:

Development
-----------

Install the ``starships-of-war`` packages (in your VM, preferable) using ``pip``:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ pip install

.. _testing:

Testing
-------

Run the tests:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ python2 setup.py test
    $ python3 setup.py test
