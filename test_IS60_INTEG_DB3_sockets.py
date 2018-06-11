
def test_ssh_socket(host):
    listening = host.socket.get_listening_sockets()
    for spec in (
"tcp://128.168.160.192:9160",
"tcp://128.168.160.192:9042",
"tcp://128.168.160.192:7000",
"tcp://128.168.160.192:16163",
"tcp://127.0.0.1:631",
"tcp://127.0.0.1:32000",
"tcp://127.0.0.1:2208",
"tcp://127.0.0.1:2207",
"tcp://:::6001",
"tcp://:::22",
"tcp://:::10050",
"tcp://0.0.0.0:912",
"tcp://0.0.0.0:6001",
"tcp://0.0.0.0:5901",
"tcp://0.0.0.0:5900",
"tcp://0.0.0.0:5801",
"tcp://0.0.0.0:111",
"tcp://0.0.0.0:11000",
"tcp://0.0.0.0:10050",


    ):
        socket = host.socket(spec)
        assert socket.is_listening

