import argparse


def convert(old_state_file: str):
    with open(old_state_file, "r", encoding="latin-1"):
        pass


def get_parser():
    parser = argparse.ArgumentParser(description="Convert Zino1 state to Zino2 compatible state")
    parser.add_argument(
        "statedump",
        help="Absolute path to the Zino1 state you want to convert",
    )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    convert(args.statedump)


if __name__ == "__main__":
    main()
