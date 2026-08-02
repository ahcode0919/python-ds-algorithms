def reverse_words_ii(sentence: list[str]):
    """Reverse Words In A Sentence II.

    Reverse the order of the words in a sentence. The sentence is given as an array of characters separated by
    spaces, and must be reversed in place.

    Example: `["a", " ", "b", "o", "y"]` -> `["b", "o", "y", " ", "a"]`

    Reverse the whole character array, then reverse each individual word back to its original order.
    """

    def reverse(string: list[str], left: int, right: int):
        """Reverse string[left:right] in place using a two-pointer swap."""
        while left < right:
            string[left], string[right] = string[right], string[left]
            left += 1
            right -= 1

    length = len(sentence)
    reverse(sentence, 0, length - 1)
    left_index = None

    for index in range(length):
        if left_index is None and sentence[index] != " ":
            left_index = index
        if sentence[index] == " ":
            reverse(sentence, left_index, index - 1)
            left_index = None

    if left_index is not None:
        reverse(sentence, left_index, length - 1)
