ARK
====

Assists with Iowa State University EZID ARK assignment in contentDM.


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

Dependencies
-------------

* chromedriver.exe: https://sites.google.com/a/chromium.org/chromedriver/
* ezid.py: https://ezid.cdlib.org/doc/ezid.py
* batch-download.sh: https://ezid.cdlib.org/doc/batch-download.sh
