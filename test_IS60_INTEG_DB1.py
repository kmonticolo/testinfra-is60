# userzy uslugi procesy pliki filesystemy centos

def test_uname_output(Command):
    command = Command('uname -s')
    assert command.stdout.rstrip() == 'Linux'
    assert command.rc == 0

def test_NTP_ntpstat(Command):
    command = Command('ntpstat')
    assert command.rc == 0

def test_root_user(host):
    user = host.user("root")
    assert user.exists
    assert user.uid == 0
    assert user.gid == 0
    assert user.name == "root"
    assert user.group == "root"
    assert user.groups == [ "root", "bin", "daemon", "sys", "adm", "disk", "wheel" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/root"

def test_seachange_user(host):
    user = host.user("seachange")
    assert user.exists
    assert user.uid == 500
    assert user.gid == 500
    assert user.name == "seachange"
    assert user.group == "seachange"
    assert user.groups == [ "seachange", "wheel", "haclient" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/home/seachange"

def test_mysql_user(host):
    user = host.user("mysql")
    assert user.exists
    assert user.uid == 102
    assert user.gid == 104
    assert user.name == "mysql"
    assert user.group == "mysql"
    assert user.groups == ["mysql"]
    assert user.shell == "/bin/bash"
    assert user.home == "/var/lib/mysql"

def test_hacluster_user(host):
    user = host.user("hacluster")
    assert user.exists
    assert user.uid == 498
    assert user.gid == 496
    assert user.name == "hacluster"
    assert user.group == "haclient"
    assert user.groups == ["haclient"]
    assert user.shell == "/bin/bash"
    assert user.home == "/var/lib/heartbeat/cores/hacluster"


def test_haclient_group_exists(Group):
    group = Group('haclient')
    assert group.exists

def test_seachange_group_exists(Group):
    group = Group('seachange')
    assert group.exists

def test_mysql_group_exists(Group):
    group = Group('mysql')
    assert group.exists

def test_cassandra_service_exists(host):
    service = host.service("cassandra")
    assert service.is_running
    assert service.is_enabled

def test_drbd_service_exists(host):
    service = host.service("drbd")
    assert service.is_running
    assert service.is_enabled

def test_drbd_status(Command):
    command = Command('service drbd status')
    assert command.rc == 0

def test_drbdadm_cstate(Command):
    command = Command('drbdadm cstate all')
    assert command.rc == 0

def test_drbd_package(host):
    package= host.package("drbd83-8.3.8-1.el5.centos")
    assert package.is_installed
    assert package.version.startswith("8.3.")

def test_kmod_package(host):
    package= host.package("kmod-drbd83-8.3.8-1.el5.centos")
    assert package.is_installed
    assert package.version.startswith("8.3.")

def test_mysqlserver_package(host):
    package= host.package("MySQL-server-enterprise-5.1.37-0.rhel5")
    assert package.is_installed
    assert package.version.startswith("5.1.37")

def test_mysqlquery_package(host):
    package= host.package("mysql-query-browser-5.0r12-1rhel4")
    assert package.is_installed
    assert package.version.startswith("5.0r12")

def test_pgsql_package(host):
    package= host.package("postgresql-libs-8.1.22-1.el5_5.1")
    assert package.is_installed
    assert package.version.startswith("8.1.22")

def test_mysqladministrator_package(host):
    package= host.package("mysql-administrator-5.0r12-1rhel4")
    assert package.is_installed
    assert package.version.startswith("5.0")

def test_cassandra_nodetool(Command):
    command = Command('/seachange/local/apache-cassandra-latest/bin/nodetool -h localhost  -p 11000 statusbinary')
    assert command.stdout.rstrip() == 'running'
    assert command.rc == 0


def test_ssh_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
        "tcp://22",
        "tcp://0.0.0.0:22",
        "tcp://127.0.0.1:22",
        "tcp://:::22",
        "tcp://::1:22",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

def test_cassandra_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
        "tcp://0.0.0.0:11000",
        "tcp://127.0.0.1:32000",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

def test_cassandra_cli_getInfusionInfo(Command):
    command = Command('/seachange/local/utils/./getInfusionInfo.sh CG')
    assert command.rc == 0






#
#paczki
#drbd83-8.3.8-1.el5.centos
#kmod-drbd83-8.3.8-1.el5.centos
##[root@IS60_INTEG_DB1 seachange]# rpm -aq|grep -i sql
#MySQL-server-enterprise-5.1.37-0.rhel5
#mysql-query-browser-5.0r12-1rhel4
#postgresql-libs-8.1.22-1.el5_5.1
#sqlite-3.3.6-5
#mysql-gui-tools-5.0r12-1rhel4
#MySQL-shared-compat-5.1.37-0.rhel5
#MySQL-client-enterprise-5.1.37-0.rhel5
#python-sqlite-1.1.7-1.2.1
#mysql-administrator-5.0r12-1rhel4
#
#
#interfejsy
#
#komendy
#drbd-overview
#
# /seachange/local/apache-cassandra-latest/bin/nodetool -h localhost  -p 11000 status
#
#
#netstat 
#[root@IS60_INTEG_DB1 seachange]# netstat -alnp|grep LIST
#tcp        0      0 127.0.0.1:2208              0.0.0.0:*                   LISTEN      5028/hpiod
#tcp        0      0 127.0.0.1:32000             0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 0.0.0.0:10050               0.0.0.0:*                   LISTEN      5229/zabbix_agentd
#tcp        0      0 128.168.160.190:16163       0.0.0.0:*                   LISTEN      5498/java
#tcp        0      0 128.168.160.190:9160        0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 0.0.0.0:5801                0.0.0.0:*                   LISTEN      5440/Xvnc
#tcp        0      0 0.0.0.0:5900                0.0.0.0:*                   LISTEN      6574/Xorg
#tcp        0      0 0.0.0.0:5901                0.0.0.0:*                   LISTEN      5440/Xvnc
#tcp        0      0 0.0.0.0:53103               0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 0.0.0.0:111                 0.0.0.0:*                   LISTEN      3584/portmap
#tcp        0      0 0.0.0.0:6001                0.0.0.0:*                   LISTEN      5440/Xvnc
#tcp        0      0 128.168.160.190:9042        0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 0.0.0.0:851                 0.0.0.0:*                   LISTEN      3637/rpc.statd
#tcp        0      0 127.0.0.1:631               0.0.0.0:*                   LISTEN      5055/cupsd
#tcp        0      0 128.168.160.190:7000        0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 0.0.0.0:5560                0.0.0.0:*                   LISTEN      5448/mgmtd
#tcp        0      0 0.0.0.0:11000               0.0.0.0:*                   LISTEN      4651/java
#tcp        0      0 127.0.0.1:2207              0.0.0.0:*                   LISTEN      5033/python
#tcp        0      0 :::10050                    :::*                        LISTEN      5229/zabbix_agentd
#tcp        0      0 :::6001                     :::*                        LISTEN      5440/Xvnc
#tcp        0      0 :::22                       :::*                        LISTEN      5046/sshd
#
# cronO
#cron usera seachange cassandry
#10 1 * * 6 /seachange/local/apache-cassandra-latest/nodetool -h 128.168.160.190 -p 11000 repair -pr >> /var/log/seachange/repair.log

