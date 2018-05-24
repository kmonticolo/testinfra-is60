# userzy uslugi procesy pliki filesystemy centos

def test_uname_output(Command):
    command = Command('uname -s')
    assert command.stdout.rstrip() == 'Linux'
    assert command.rc == 0


