:hide-toc:

.. include:: ./links.inc

.. raw:: html

    <style type="text/css">h1 {display:none;}</style>

Brain Streaming Layer
=====================

.. image:: _static/icon-with-name/icon-with-name.svg
    :alt: BSL
    :class: logo
    :align: center

.. warning::

    Development of BSL is discontinued in favor of `MNE-LSL <mne-lsl_>`_. The trigger
    module has been moved to the package
    `byte-triggers <https://github.com/fcbg-platforms/byte-triggers>`_.

Open-source Python package for real-time brain signal streaming framework
based on the `Lab Streaming Layer (LSL) <lsl intro_>`_.

Install
-------

``BSL`` is available on `PyPI <project pypi_>`_ and is distributed with a compatible
version of `liblsl <lsl lib c++_>`_. If you want to use a different version of
``liblsl``, please refer to the :ref:`install:Advance install`.

.. tab-set::

    .. tab-item:: PyPI

        .. code-block:: console

            $ pip install bsl

    .. tab-item:: Source

        .. code-block:: console

            $ pip install git+https://github.com/fcbg-platforms/bsl

Supporting institutions
-----------------------

The development of ``BSL`` is supported by the
`Fondation Campus Biotech Geneva <fcbg_>`_.

.. image:: _static/partners/FCBG.svg
    :alt: FCBG - M/EEG-NMOD Platform
    :width: 150

.. toctree::
    :hidden:

    install.rst
    api/index.rst
    command_line.rst
    generated/tutorials/index.rst
