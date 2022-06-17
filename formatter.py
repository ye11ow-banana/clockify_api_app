"""
This module is used to create the output
for `Clockify.me` service data.
"""
import re


def pull_out_tasks_names(tasks_data: list[dict]) -> list[str] | list:
    return [task.get("name") for task in tasks_data if task.get("name")]


def convert_to_int_if_int(text: str) -> int | str:
    return int(text) if text.isdigit() else text


def serial_numbers(text: str) -> list[str | int]:
    """Convert to `int` serial numbers of the text."""
    return [convert_to_int_if_int(c) for c in re.split(r'(\d+)', text)]


def filter_tasks_by_serial_number(tasks: list[str]) -> list[str]:
    return sorted(tasks, key=serial_numbers)
