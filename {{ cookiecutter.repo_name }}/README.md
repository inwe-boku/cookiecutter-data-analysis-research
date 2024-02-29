[![MIT License](https://img.shields.io/github/license/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.svg)](https://choosealicense.com/licenses/mit/)
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/workflows/Tests/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}/actions?query=workflow%3ATests)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

<!--
    Add a DOI here as soon as you have one. Replace "DOIDOUBLEDASH" and "DOISINGLEDASH" with the
    DOI, do not replace "DOI". Note that if the DOI contains a single dash, you need to escape it
    by adding a second dash in the URL to the badge. Example:

    DOISINGLEDASH = 10.1088/2515-7620/ace0b9
    DOIDOUBLEDASH = 10.1088/2515--7620/ace0b9

    [![DOI](https://img.shields.io/badge/DOI-DOIDOUBLEDASH-blue)](https://doi.org/DOISINGLEDASH)
-->


{{cookiecutter.project_name}}
==============================


This repository contains code to produce the figures for a study, which currently work in progress.


Abstract
--------

{{cookiecutter.description}}


How to run
----------

```
# Clone the repository:
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

# Create a conda environment and install dependencies:
conda env update -f env.yml
conda activate {{ cookiecutter.repo_name }}

snakemake --cores all
```
