from .util import create_parser, get_default_password_length
from .generator import generator


def main() -> None:
    parser = create_parser(
        program_name="passpick",
        description="A picky password picker"
    )

    args = parser.parse_args()
    length = int(args.length or get_default_password_length(args.passphrase))

    if args.passphrase:
        print(generator.passphrase(length))
    else:
        print(generator.password(length))
