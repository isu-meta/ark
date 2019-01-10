ARK
====

Assigns ARKS to Iowa State University contentDM objects. 


Getting Started
----------------

Code requires access to a contentDM server and an EZID account.

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

#### Batch Download

If you have trouble running batch-download.sh, try the following.

``` {.sourceCode .console}
$ sudo apt-get install dos2unix
$ dos2unix batch-download.sh
```


Dependencies
-------------

* chromedriver.exe: https://sites.google.com/a/chromium.org/chromedriver/
* ezid.py: https://ezid.cdlib.org/doc/ezid.py
* batch-download.sh: https://ezid.cdlib.org/doc/batch-download.sh
