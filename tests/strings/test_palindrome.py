from src.strings.palindrome import valid_palindrome, valid_palindrome_naive


def test_valid_palindrome_naive():
    assert valid_palindrome_naive("aba")
    assert not valid_palindrome_naive("aacbaa")
    assert not valid_palindrome_naive("a:bba")


def test_valid_palindrome():
    assert valid_palindrome("aba ")
    assert valid_palindrome("aba")
    assert not valid_palindrome("aacbaa")
    assert valid_palindrome("a:bba")
