js.d3
=====

Introduction
------------

This library packages `D3.js`_ for `Fanstatic`_.

.. _`Fanstatic`: http://fanstatic.org
.. _`D3.js`: http://d3js.org

This requires integration between your web framework and ``Fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.d3``) are published to some URL. This
library also packages up a minified version of `D3.js`_.


Usage
-----

.. note::

   At present, D3 does not support any browser that lacks SVG support. This
   means that Internet Explorer 8 and below will produce errors if the D3 
   library is loaded.  To work around this, ``js.d3`` includes a conditional 
   comment to restrict D3 to Internet Explorer 9 or above.

You can import ``d3`` from ``js.d3`` and ``need`` it where you want these
resources to be included on a page::

  >>> from js.d3 import d3
  >>> d3.need()


Updating this package
---------------------

In order to obtain a newer version of this library, do the following,
editing the version name (eg ``3.1.5``) accordingly::

    pushd js/d3/resources
    wget https://github.com/mbostock/d3/raw/v3.1.5/d3.js -O d3.js
    wget https://github.com/mbostock/d3/raw/v3.1.5/d3.min.js -O d3.min.js
    popd
    #Edit changelog, setup.py for versions, etc
    git commit -a -m "Updated for release 3.1.5"
    git push
