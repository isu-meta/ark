ARK
====

A jupyter notebook to assist with ARK assignment of contentDM collection.

Getting Started
----------------

To run this code, you need to have access to a contentDM server, as well as an EZID 
account. 

Clone the repository and create an anaconda environment.

``` {.sourceCode .console}
$ git clone https://github.com/wryan14/ark.git
$ cd ark
$ conda create -n "ark_env" python=2.7
$ activate ark_env
$ pip install -r requirements.txt
```

With the environment created, run via jupyter notebook.

``` {.sourceCode .console}
$ jupyter notebook
```

Credits
--------

chromedriver.exe: https://sites.google.com/a/chromium.org/chromedriver/
ezid.py: https://ezid.cdlib.org/doc/ezid.py
batch-download.sh: https://ezid.cdlib.org/doc/batch-download.sh
