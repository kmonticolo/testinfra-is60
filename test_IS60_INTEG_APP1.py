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
    assert user.groups == [ "seachange", "wheel" ]
    assert user.shell == "/bin/bash"
    assert user.home == "/home/seachange"




def test_seachange_group_exists(Group):
    group = Group('seachange')
    assert group.exists








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
        "tcp://127.0.0.1:32000",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

