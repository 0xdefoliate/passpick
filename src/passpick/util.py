import argparse


def create_parser(program_name: str, description: str) -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        prog=program_name,
        description=description
    )

    arg_parser.add_argument("--passphrase", "-p", action="store_true")
    arg_parser.add_argument("--length", "-L")

    return arg_parser


def get_default_password_length(is_passphrase: bool) -> int:
    if is_passphrase:
        return 6 # words

    return 64 # characters
