for DB: py.test --ssh-config=/home/kamil/.ssh/config --hosts IS60_INTEG_DB1,IS60_INTEG_DB2,IS60_INTEG_DB1,IS60_INTEG_DB3
for APP: py.test test_IS60_INTEG_APP1.py --ssh-config=/home/kamil/.ssh/config --hosts IS60_INTEG_APP1
but I will try tox to spawn them in a more efficient way
where /home/kamil/.ssh/config is configuration which allows you to connect to IS60 site

and you need to install testinfra: pip install testinfra
i put my tests into https://gitlab.dcclabs.tv/kmonticolo/is60-tests

testowanie: 

 py.test --ssh-config=/home/kamil/.ssh/config --hosts IS60_INTEG_DB1
