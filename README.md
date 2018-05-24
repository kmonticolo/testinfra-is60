# IS60 infrastructure tests

## installation: 

`$ pip install testinfra`

## execution

for DB: `py.test --ssh-config=/home/kamil/.ssh/config --hosts IS60_INTEG_DB1,IS60_INTEG_DB2,IS60_INTEG_DB1,IS60_INTEG_DB3`

for APP: `py.test test_IS60_INTEG_APP1.py --ssh-config=/home/kamil/.ssh/config --hosts IS60_INTEG_APP1 -v`


where /home/kamil/.ssh/config is configuration which allows you to connect to IS60 site


