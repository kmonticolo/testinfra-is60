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

def test_zabbix_agent_service_exists(host):
    service = host.service("zabbix-agent")
    assert service.is_running
    assert service.is_enabled

#def test_rhq_agent_service_exists(host):
#    service = host.service("rhq-agent")
#    assert service.is_running
#    assert service.is_enabled

def test_rhq_agent_running(Command):
    command = Command('sudo service rhq-agent status')
    assert command.rc == 0


def test_infusion_service_exists(host):
    service = host.service("infusion")
    assert service.is_running
    assert service.is_enabled

def test_ads_package(host):
    package= host.package("ads-6.0.0")
    assert package.is_installed
    assert package.version.startswith("6.0.0")

def test_usm_ads_strmanager_package(host):
    package= host.package("usm-ads-streamingstoragemanager-2.0.1")
    assert package.is_installed
    assert package.version.startswith("2.0.1")

def test_usm_ads_package(host):
    package= host.package("usm-ads-2.0.1")
    assert package.is_installed
    assert package.version.startswith("2.0.1")

def test_usm_ads_mcast_package(host):
    package= host.package("usm-ads-mcastreamer-2.0.1")
    assert package.is_installed
    assert package.version.startswith("2.0.1")

def test_pcs_package(host):
    package= host.package("pcs-6.0.0")
    assert package.is_installed
    assert package.version.startswith("6.0.0")

def test_adr_scripts_package(host):
    package= host.package("adrenalin-deploy-scripts-for-IS60-2.3.0")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_adr_util_package(host):
    package= host.package("adrenalin-utilities-for-IS60-2.3.0")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

def test_adr_package(host):
    package= host.package("adr-6.0.0")
    assert package.is_installed
    assert package.version.startswith("6.0.0")

def test_rsyslog_package(host):
    package= host.package("seachange-rsyslog-client-for-IS60-2.3.0")
    assert package.is_installed
    assert package.version.startswith("2.3.0")

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

def test_app_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
        "tcp://127.0.0.1:32000",
    ):
        socket = host.socket(spec)
        assert socket.is_listening

