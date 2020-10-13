# Python Installer Guide

## Prereqs
`sudo apt-get install build-essential checkinstall`  
```bash
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
    libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
```

Needed ?  
+ `wget ...bzip2_latest.tar.gz`
+ `tar xf ...`
+ `make; sudo make install`


## Install
+ `wget https://www.python.org/ftp/python/3.8.3/Python-3.8.3.tgz`
+ `tar xzf Python-3.8.3.tgz`

+ `cd Python-3.8.3`
+ `sudo ./configure --enable-loadable-sqlite-extensions --enable-optimizations`
+ `make` (; `make test`)
+ `sudo make altinstall` (doesn't replace /usr/bin/python)


## Deps
+ `pip3.7 install pysqlite2 pysqlite3 db-sqlite3`
+ `pip3.7 install pandas jupyter bokeh "holoviews[recommended]"`
  + bokeh issues - https://github.com/bokeh/bokeh/issues/7005, 

---

# Bibliography
https://tecadmin.net/install-python-3-8-ubuntu/