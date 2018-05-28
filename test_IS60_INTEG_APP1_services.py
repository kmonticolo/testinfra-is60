def test_httpd_service_exists(host):
    service = host.service("httpd")
    assert service.is_running
    assert service.is_enabled


