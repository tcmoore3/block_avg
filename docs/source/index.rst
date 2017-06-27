.. block_avg documentation master file, created by
   sphinx-quickstart on Tue Jun 27 16:11:46 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

block_avg
=========
*A package for computing block averages of numerical data*

Computing block averages is easy::

    import numpy as np
    import block_avg as ba

    data = np.loadtxt('data.txt')
    data, stds = ba.block_avg(data, 100)

There is currently one function in this package.

.. autofunction:: block_avg.block_avg

.. toctree::
   :maxdepth: 2

