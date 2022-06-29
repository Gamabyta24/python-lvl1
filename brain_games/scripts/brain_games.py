#!/usr/bin/env python
"""Test."""


import prompt


def welcome_user():
    """Public func."""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello,{name}!")


def main():
    """Enter point."""
    welcome_user()


if __name__ == "__main__":
    main()
