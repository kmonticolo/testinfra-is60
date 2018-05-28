#!/bin/sh

# appservers
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP1_sockets.py test_IS60_INTEG_APP1_services.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.193  -v -n4
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP2_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.194  -v -n4
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP3_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.195  -v -n4
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP4_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.196  -v -n4
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP5_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.197  -v -n4
py.test test_IS60_INTEG_APP_common.py test_IS60_INTEG_APP6_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.198  -v -n4

#databases with drbd
py.test test_IS60_INTEG_DB_common.py test_IS60_INTEG_DB_drbd.py test_IS60_INTEG_DB1_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.190 -v -n4
py.test test_IS60_INTEG_DB_common.py test_IS60_INTEG_DB_drbd.py test_IS60_INTEG_DB2_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.191 -v -n4

# without drbd
  py.test test_IS60_INTEG_DB_common.py test_IS60_INTEG_DB3_sockets.py --ssh-config=/tmp/sshconfig --hosts 128.168.160.192  -v -n4
