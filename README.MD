# Alami Test Processing Data from CSV

## Prerequisites

- Python3 (>= v3.6 is recommended)
   Follow this tutorial : [Installing Python3](http://docs.python-guide.org/en/latest/starting/installation/#python-3-installation-guides) or [Setup Python3 on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-16-04#step-2-%E2%80%94-setting-up-a-virtual-environment)

## Installation & Running

After prerequisites has been setup. You have to make the program run. 
  - Install `python` ( >= v3.6 is recommended), `pip`, `virtualenv`
  - go to inside directory `alami-test-project/`
  - Acitvation python virtualenv with this command `source venv/bin/activate`
  - there are 2 files, first is `non_thread_mechanism.py` and the second is `thread_mechanism.py` 
  - if you want execute without thread mechanism just using this command `python non_thread_mechanism.py` that script will read data from `Before Eod.csv` and write the result into this file `After Eod.csv`
  - if you want execute with thread mechanism just using this command `python thread_mechanism.py` that script will read data from `Before Eod.csv` and write the result into these files `After Eod_1.csv, After Eod_2.csv, After Eod_3.csv, After Eod_4.csv`, each file have 50 data, because i'm use 4 thread for writing result into csv file.

Last but not least, if you have question or facing a problem, you can reach me at `ilhamsyaifulakbar18@gmail.com`.

Thanks !!