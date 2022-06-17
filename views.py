"""
This module is used to output `Clockify.me` data.
"""
from typing import Iterable


def print_list_elements(elements: Iterable) -> None:
    for element in elements:
        print(element)


def show_error_message(message: str) -> None:
    print(message)
