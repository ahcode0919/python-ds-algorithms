from strings.license_key_formatter import license_key_formatter


def test_license_key_formatter():
    assert license_key_formatter('5F3Z-2e-9-w', 4) == '5F3Z-2E9W'
    assert license_key_formatter('5F3Z-2e-9-w', 3) == '5F-3Z2-E9W'
    assert license_key_formatter('TES-T', 4) == 'TEST'
    assert license_key_formatter('t-est', 2) == 'TE-ST'
