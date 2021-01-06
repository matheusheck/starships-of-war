.. image:: https://travis-ci.org/lukassup/python-cli.svg?branch=master
    :target: https://travis-ci.org/lukassup/python-cli

starships-of-war
========

``starships-of-war`` is a simple Python CLI CRUD application to rank starships by
Hyperdriver or Sublight speed.



Usage
-----

Have a service to rank the StarWars Ships by HyperDrive Class easy.
Here data is persisted on Postgre on Docker connected on default port, to create this DB:

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

Install the ``starships-of-war`` dependencies using ``pipenv``:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ pipenv shell

.. _Use:

Use
-----------

Install the ``starships-of-war`` dependencies using ``pipenv``:

.. code-block:: bash

    $ python3 

.. _testing:

Testing
-------

Run the tests:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war
    $ python3 setup.py test
