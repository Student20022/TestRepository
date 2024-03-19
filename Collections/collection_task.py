from collections import Counter


def once_presented_chars_num(string: str) -> int:
    if not isinstance(string, str):
        raise TypeError("Function takes only str type")

    once_presented_char_num = sum(
        1 for value in Counter(string).values() if value == 1)

    return once_presented_char_num
