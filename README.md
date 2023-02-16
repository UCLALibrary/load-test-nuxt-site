.. _installation:

Installation
============

0. `Install Python <https://docs.python-guide.org/starting/installation/>`_ (3.7 or later)

1. Install the package (check `the wiki <https://github.com/locustio/locust/wiki/Installation>`_ if the installation fails)

.. code-block:: console

    $ pip3 install locust


Load Test
============

.. code-block:: console

    OFC-ML-DIIT004:load-test-nuxt-site parinitamulak$ locust -f locust_nuxt_website_most_visited_pages.py
    [2023-02-15 10:38:27,264] OFC-ML-DIIT004/INFO/locust.main: Starting web interface at http://0.0.0.0:8089 (accepting connections from all network interfaces)
    [2023-02-15 10:38:27,283] OFC-ML-DIIT004/INFO/locust.main: Starting Locust 2.14.2


