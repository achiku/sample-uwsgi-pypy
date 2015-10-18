# sample-uwsgi-pypy
Sample setup for uwsgi + pypy

## Install pypy

- http://uwsgi-docs.readthedocs.org/en/latest/PyPy.html
- https://github.com/unbit/uwsgi/tree/uwsgi-2.0/plugins/pypy


### OSX

uwsgi + pypy might not work on OSX because of this issue. I'm trying out Ubuntu 14.10.

- https://github.com/Homebrew/homebrew/issues/32642

```
$ brew update
$ brew install pypy
```

### Ubuntu 14.10

```
$ sudo apt-get update
$ sudo apt-get install pypy
```


## Set up vertualenv

```
$ virtualenv venv --python=pypy
$ source venv/bin/activate
$ pip install -r requirements.txt
```


## Check if pypy plugin is enabled

```
$ uwsgi --version
2.0.11.1
$ uwsgi --help | grep pypy
Usage: /Users/achiku/work/achiku/sample-uwsgi-pypy/venv/bin/uwsgi [options...]
    --pypy-lib                            set the path/name of the pypy library
    --pypy-setup                          set the path of the python setup script
    --pypy-home                           set the home of pypy library
    --pypy-wsgi                           load a WSGI module
    --pypy-wsgi-file                      load a WSGI/mod_wsgi file
    --pypy-ini-paste                      load a paste.deploy config file containing uwsgi section
    --pypy-paste                          load a paste.deploy config file
    --pypy-eval                           evaluate pypy code before fork()
    --pypy-eval-post-fork                 eval
```
