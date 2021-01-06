starships-of-war
========

``starships-of-war`` is a simple Python CRUD service to rank starships by
Hyperdriver or Sublight speed. 

Running this __main__.py the CLI connects to a Postgre Database,
check the ships result and insert if running the 1st time, call a method to retrieve 
a list of all starships from the Star Wars movies, sorted by the hyperdrive rating 
(the faster the hyperdrive, the lower warp drive rating.).

This db assumes -1 value for non hyperdrive modules.



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

Development mode
-----------

Install the ``starships-of-war`` dependencies using ``pipenv``:

.. code-block:: bash

    $ git clone https://github.com/matheusheck/starships-of-war.git
    $ cd starships-of-war

.. _Use:

Run using ``pipenv``:

.. code-block:: bash

    $ pipenv shell
    $ pipenv run python __main__.py   


