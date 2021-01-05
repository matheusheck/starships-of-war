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

Rank the Startwars Ships easy: Choose for Hyperdrive or sublight speed and compare.
Here the Postgres connects the default port on Docker:

.. code-block::

    $ docker run --name sqlalchemy-orm-psql \
      -e POSTGRES_PASSWORD=pass \
      -e POSTGRES_USER=usr \
      -e POSTGRES_DB=starships \
      -p 5432:5432 \
      -d postgres

Run starships-of-war

.. _development:

Development
-----------

Install the ``starships-of-war`` depedencies using ``pipenv``:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ pipenv shell

.. _testing:

Testing
-------

Run the tests:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ python3 setup.py test
