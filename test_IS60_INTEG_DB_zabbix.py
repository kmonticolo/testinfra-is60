
def test_diskstats_zabbix_conf(File):
    file= File("/etc/zabbix/zabbix_agentd.d/userparameter_diskstats.conf")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644


def test_drbd_zabbix_conf(File):
    file= File("/etc/zabbix/zabbix_agentd.d/userparameter_drbd.conf")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644


def test_pacemaker_zabbix_conf(File):
    file= File("/etc/zabbix/zabbix_agentd.d/zabbix-agent-pacemaker.conf")
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o644


def test_pacemaker_actions(File):
    file= File("/usr/local/bin/check_pacemaker_actions")
    assert file.user == "root"
    assert file.group == "root"


def test_crm_mon_stats(File):
    file= File("/usr/local/bin/crm_mon_stats.sh")
    assert file.user == "root"
    assert file.group == "root"

def test_sudoers(Command):
    command = Command('sudo grep zabbix /etc/sudoers')
    assert command.stdout.rstrip() == 'zabbix	ALL=(ALL)	NOPASSWD: /sbin/drbdadm, /usr/local/bin/check_pacemaker_actions, /usr/local/bin/crm_mon_stats.sh'
    assert command.rc == 0

