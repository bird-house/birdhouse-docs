.. _letsencrypt:

Using Let's encrypt to generate a certificte
============================================

One can use the `Let's Encrypt <https://letsencrypt.org/>`_ service to generate automatically
a valid x509 certificate for web-services.

Debian/Ubuntu
-------------

Instructions on: https://certbot.eff.org/#ubuntutyakkety-nginx

Enable certbot ubuntu repo:

.. code-block:: sh

  $ sudo apt-get update
  $ sudo apt-get install software-properties-common
  $ sudo add-apt-repository ppa:certbot/certbot
  $ sudo apt-get update

Install certbot for nginx:

.. code-block:: sh

  $ sudo apt-get install python-certbot-nginx



Links
-----

* https://letsencrypt.org/
