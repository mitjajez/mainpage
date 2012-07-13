*wlan slovenija* main webpage
=============================

Development installation
------------------------

1. Clone from GitHub_ both webpage and nodewatcher_ repositories::

    git clone https://github.com/wlanslovenija/mainpage.git
    git clone https://github.com/wlanslovenija/nodewatcher.git

   You can also use SSH-based URLs or URLs of your fork.

2. Create and activate new `Python virtual environment`_::

    virtualenv --no-site-packages ~/.virtualenv/mainpage
    source ~/.virtualenv/mainpage/bin/activate
    
3. Move to location where you cloned webpage repository and run ``devsetup``
   script::

    python scripts/devsetup.py
    
   This script will install all requirements and import database dump to local database.

4. Run::

    python manage.py runserver

   and start developing!

You can safely rerun the ``devsetup`` as needed, but be advised that database
content might not be preserved or might get corrupted. In the latter case,
simply delete ``db.sqlite`` file and run the script again.

.. _GitHub: https://github.com/
.. _nodewatcher: http://dev.wlan-si.net/wiki/Nodewatcher
.. _Python virtual environment: http://www.virtualenv.org
