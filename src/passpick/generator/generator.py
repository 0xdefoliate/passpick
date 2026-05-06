import secrets

from passpick.dataset.words import WORDS


def passphrase(word_count: int, separator: str = "-") -> str:
    words = []

    for i in range(word_count):
        word = secrets.choice(WORDS)
        words.append(word)

    return separator.join(words)


def password(length: int) -> str:
    return secrets.token_hex(128)[:length]
