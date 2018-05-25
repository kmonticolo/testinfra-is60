def test_drbd_service_exists(host):
    service = host.service("drbd")
    assert service.is_running
    assert service.is_enabled

def test_drbd_status(Command):
    command = Command('/sbin/service drbd status')
    assert command.rc == 0

def test_drbdadm_cstate(Command):
    command = Command('/sbin/drbdadm cstate all')
    assert command.rc == 0

def test_drbd_package(host):
    package= host.package("drbd83-8.3.8-1.el5.centos")
    assert package.is_installed
    assert package.version.startswith("8.3.")

def test_kmod_package(host):
    package= host.package("kmod-drbd83-8.3.8-1.el5.centos")
    assert package.is_installed
    assert package.version.startswith("8.3.")
