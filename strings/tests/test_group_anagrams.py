from strings.group_anagrams import group_anagrams


def test_group_anagrams():
    strings = []
    assert group_anagrams(strings) == []

    strings = ['test']
    assert group_anagrams(strings) == [['test']]

    strings = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
    assert group_anagrams(strings) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
