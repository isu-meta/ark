ARK
====

Assigns ARKS to Iowa State University contentDM objects. 


Getting Started
----------------

Code requires access to a CONTENTdm server and an EZID account.

Clone the repository and create a virtual environment.

``` {.sourceCode .console}
$ git clone https://github.com/isu-meta/ark.git
$ cd ark
$ python -m venv "ark_env"
$ ark_env\Scripts\activate ark_env
$ pip install -r requirements.txt
```

With the environment created, run via jupyter notebook.

``` {.sourceCode .console}
$ jupyter notebook
```

In Jupyter Notebook, open "cdm_script.ipynb."

#### Batch Download

To download a list of current ARKs, in the Command Prompt, run:

``` {.sourceCode .console}
> python batch_download.py <username> <password> format=xml type=ark compression=zip
```

Dependencies
-------------

* chromedriver.exe: https://sites.google.com/a/chromium.org/chromedriver/
* ezid.py: https://ezid.cdlib.org/doc/ezid.py

Documentation
--------------

Please note that the current documentation link details the use of
the deprecated Python 2 version of this notebook and related scripts.
Much of it is still relevant, but some practices and commands have changed.

The documentation will be updated as time allows.

https://mddocs.readthedocs.io/en/latest/arks.html

