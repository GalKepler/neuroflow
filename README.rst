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
      - |github-actions| |codecov| |codacy|
    * - pypi & updates
      - |black| |isort| |flake8| |pre-commit|

.. |codacy| image:: https://app.codacy.com/project/badge/Grade/6acd65a8fd4741509422510d7a023386
    :target: https://app.codacy.com/gh/GalKepler/neuroflow/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
    :alt: Code Quality

.. |docs| image:: https://readthedocs.org/projects/neuroflow/badge/?style=flat
    :target: https://readthedocs.org/projects/neuroflow/
    :alt: Documentation Status

.. |github-actions| image:: https://github.com/GalKepler/neuroflow/actions/workflows/github-actions.yml/badge.svg
    :alt: GitHub Actions Build Status
    :target: https://github.com/GalKepler/neuroflow/actions

.. |codecov| image:: https://codecov.io/github/GalKepler/neuroflow/graph/badge.svg?token=LO5CH471O4
    :alt: Coverage Status
    :target: https://app.codecov.io/github/GalKepler/neuroflow

.. |black| image:: https://img.shields.io/badge/formatter-black-000000
        :target: https://github.com/psf/black

.. |isort| image:: https://img.shields.io/badge/imports-isort-%231674b1
    :alt: isort
    :target: https://pycqa.github.io/isort/

.. |flake8| image:: https://img.shields.io/badge/style-flake8-000000
    :alt: Flake8
    :target: https://flake8.pycqa.org/en/latest/

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
    :alt: pre-commit
    :target: https://github.com/pre-commit/pre-commit


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
