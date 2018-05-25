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

def test_zabbix_agent_service_exists(host):
    service = host.service("zabbix-agent")
    assert service.is_running
    assert service.is_enabled

def test_cassandra_service_exists(host):
    service = host.service("cassandra")
    assert service.is_running
    assert service.is_enabled

def test_cassandra_commitlog_on_other_disk(Command):
    command = Command('mount |grep /dev/sdd.*/var/data/cassandra/commitlog')
    assert command.rc == 0

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


# TODO
#interfejsy
#
#komendy
#drbd-overview
#
# /seachange/local/apache-cassandra-latest/bin/nodetool -h localhost  -p 11000 status
#
