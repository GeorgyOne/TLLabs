"""Command line interface for TLLabs."""

import argparse


def main(argv=None):
    parser = argparse.ArgumentParser(description="TLLabs CLI")
    parser.add_argument(
        "--greet",
        default="Hello from TLLabs",
        help="Greeting message to display",
    )
    args = parser.parse_args(argv)
    print(args.greet)


if __name__ == "__main__":
    main()
