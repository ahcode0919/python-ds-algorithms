# Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you
#  would be asked to do during a real interview.
#
# Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character,
#  return '_'.
def firstNotRepeatingCharacter(s):
    length = len(s)
    index = 0
    while index < length:
        if s[index] not in s[:index] and s[index] not in s[index+1:]:
            return s[index]
        index += 1
    return '_'

def test_firstNotRepeatingCharacter():
    assert firstNotRepeatingCharacter('aaaaabc') == 'b'
    assert firstNotRepeatingCharacter('aaaaaa') == '_'

def firstNotRepeatingCharacter2(s):
    checkedChars = set() #skip characters we've already checked.
    for char in s:
        if char not in checkedChars and s.index(char) == s.rindex(char):
            return char
        checkedChars.add(char)
    return '_'

def test_firstNotRepeatingCharacter2():
    assert firstNotRepeatingCharacter2('aaaaabc') == 'b'
    assert firstNotRepeatingCharacter2('aaaaaa') == '_'