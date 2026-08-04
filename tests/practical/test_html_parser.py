import pytest

from src.practical.html_parser import HTMLValidator


def test_html_file_validator():
    assert HTMLValidator.validate_html("tests/practical/test_data/valid.html") is True
    assert HTMLValidator.validate_html("tests/practical/test_data/invalid.html") is False


def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        assert HTMLValidator.validate_html("tests/practical/test_data/nonexistent.html") is False


def test_invalid_html():
    html = "<p>"
    assert not HTMLValidator.validate_string(html)

    html = "<p>test"
    assert not HTMLValidator.validate_string(html)

    html = "<h1><p>test</p></h1><p>"
    assert not HTMLValidator.validate_string(html)


def test_valid_html():
    html = ""
    assert HTMLValidator.validate_string(html)

    html = "<p></p>"
    assert HTMLValidator.validate_string(html)

    html = "<p>test</p><test></test>"
    assert HTMLValidator.validate_string(html)
