def reverse_words(sentence: str) -> str:
    """Reverse Words In A Sentence.

    Reverse the words in a sentence while keeping the words themselves in their original order.

    Example: `"The fox is red"` -> `"ehT xof si der"`

    Reverse the characters within each space-delimited word, left to right.
    """

    def reverse(array: list[str], left: int, right: int):
        """Reverse array[left:right] in place using a two-pointer swap."""
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    length = len(sentence)
    sentence_array = list(sentence)
    left_index = 0

    for index in range(length):
        if sentence_array[index] == " ":
            reverse(sentence_array, left_index, index - 1)
            left_index = index + 1

    # reverse last word, or sentence if one word
    reverse(sentence_array, left_index, length - 1)

    return "".join(sentence_array)
