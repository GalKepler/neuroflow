.. image:: https://github.com/GalKepler/neuroflow/blob/main/assets/neuroflow.png?raw=true
    :align: center

========
Overview
========
.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests & coverage
      - |github-actions| |codecov|
    * - pypi & updates
      - |pypi| |pyup|

.. |docs| image:: https://readthedocs.org/projects/neuroflow/badge/?style=flat
    :target: https://readthedocs.org/projects/neuroflow/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/GalKepler/neuroflow/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/GalKepler/neuroflow/actions

.. |codecov| image:: https://codecov.io/github/GalKepler/neuroflow/graph/badge.svg?token=LO5CH471O4
    :alt: Coverage Status
    :target: https://app.codecov.io/github/GalKepler/neuroflow

.. |pypi| image:: https://img.shields.io/pypi/v/neuroflow.svg
        :target: https://pypi.python.org/pypi/neuroflow

.. |pyup| image:: https://pyup.io/repos/github/GalKepler/neuroflow/shield.svg
     :target: https://pyup.io/repos/github/GalKepler/neuroflow/
     :alt: Updates



NeuroFlow: A streamlined toolkit for DWI post-processing, offering advanced analysis and visualization for neuroimaging research.


* Free software: MIT license
* Documentation: https://neuroflow.readthedocs.io.


Features
--------

* Estimation of tensor derivatives (FA, MD, AD, RD, etc.) using either `MRtrix3 <https://www.mrtrix.org/>`_ or `DIPY <https://dipy.org/>`_.
* Registration of numerous volumetric parcellation atlases to subjects' native T1w and DWI images.
* Estimation of numerous distribution metrices (e.g. mean, median, IQR-mean, etc.) of diffusion metrics within each parcellation unit.
* Automatic extraction of available covariates originating from different sources (demographics, temporal, environmental).
* Quality control of the preprocessing of the diffusion MRI data.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
