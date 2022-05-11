import re


def count_words(txt: str) -> dict:
    """
    The function accepts text as a parameter, and returns a dictionary of its words lengths.
    :param txt: A string of words
    :return: A dictionary of the text's words lengths
    """
    regex = re.compile('[^a-zA-Z]')
    words_length = {word: len(word) for word in [regex.sub('', word) for word in txt.split()]}
    return words_length


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
