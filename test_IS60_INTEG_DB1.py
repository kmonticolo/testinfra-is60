# userzy uslugi procesy pliki filesystemy centos

def test_uname_output(Command):
    command = Command('uname -s')
    assert command.stdout.rstrip() == 'Linux'
    assert command.rc == 0

def test_root_user_exists(User):
    user = User('root')
    assert user.exists

#def test_seachange_user_exists(User):
#    user = User('seachange')
#    assert user.exists
#    assert user.group == "seachange"   
#    assert user.groups == ['wheel', 'seachange', 'haclient']

def test_seachange_user(host):
    user = host.user("seachange")
    assert user.exists
    assert user.uid == 500
    assert user.gid == 500
    assert user.name == "seachange"
    assert user.group == "seachange"
    assert user.groups == ["seachange", "wheel", "haclient" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/home/seachange"

    #assert user.groups == "haclient"   


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



def test_hacluster_user_exists(User):
    user = User('hacluster')
    assert user.exists
    assert user.group == "haclient"   

def test_haclient_group_exists(Group):
    group = Group('haclient')
    assert group.exists

def test_seachange_group_exists(Group):
    group = Group('seachange')
    assert group.exists

def test_mysql_group_exists(Group):
    group = Group('mysql')
    assert group.exists





# uslugi chkconfig --list|grep on
# cassandra conman ? drbd heartbeat 
def test_cassandra_service_exists(host):
    service = host.service("cassandra")
    assert service.is_running
    assert service.is_enabled

def test_drbd_service_exists(host):
    service = host.service("drbd")
    assert service.is_running
    assert service.is_enabled

#procesy heartbeat



# procesy
# /seachange/local/apache-cassandra-1.2.18/bin/./wrapper /seachange/local/apache-cassandra-1.2.18/bin/./cassandra_wrapper.conf wrapper.syslog.ident=cassandra wrapper.pidfile=/seachange/local/apache-cassandra-1.2.18/bin/./cassandra.pid wrapper.name=cassandra wrapper.displayname=Cassandra wrapper.daemonize=TRUE wrapper.script.version=3.5.26

# pstree
#
#
#java
#
# grupa procesow heartbeat
#
#
#
#userzy
#[root@IS60_INTEG_DB1 seachange]# grep sh$ /etc/passwd
#root:x:0:0:root:/root:/bin/bash
#seachange:x:500:500::/home/seachange:/bin/bash
#mysql:x:102:104:MySQL server:/var/lib/mysql:/bin/bash
#hacluster:x:498:496::/var/lib/heartbeat/cores/hacluster:/bin/bash
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
