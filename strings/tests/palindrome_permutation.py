from strings.palindrome_permutation import palindrome_permutation


def test_palindrome_permutation():
    assert palindrome_permutation('aabb')
    assert palindrome_permutation('aab')
    assert palindrome_permutation('aba')
    assert palindrome_permutation('')
    assert not palindrome_permutation('test')
    assert not palindrome_permutation('aabc')
