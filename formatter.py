"""
This module is used to create the output
for `Clockify.me` service data.
"""
import re
from datetime import datetime
from itertools import groupby


def pull_out_tasks_names(tasks: list[dict]) -> list[str] | list:
    """
    Pull out tasks names from data about tasks
    that got from API.
    """
    return [task.get("name") for task in tasks if task.get("name")]


def _convert_to_int_if_int(string: str) -> int | str:
    return int(string) if string.isdigit() else string


def _to_int_serial_numbers(string: str) -> list[str | int]:
    """Convert to `int` serial numbers of the string."""
    return [_convert_to_int_if_int(s) for s in re.split(r'(\d+)', string)]


def sort_tasks_names_by_serial_numbers(tasks_names: list[str]) -> list[str]:
    return sorted(tasks_names, key=_to_int_serial_numbers)


def pull_out_report_data(tasks: list[dict], time_entries: list[dict]) -> list:
    """Pull out needed data for report file."""
    report_data = []

    for time_entry in time_entries:
        for task in tasks:
            if time_entry["taskId"] == task["id"]:
                desc = time_entry["description"]
                description = desc if desc else "it does\'t have a description"

                report_data.append({
                    "name": task["name"],
                    "description": description,
                    "date": time_entry["timeInterval"]["start"],
                    "duration": time_entry["timeInterval"]["duration"] or "-"
                })

    return report_data


def convert_duration_to_time_format(duration: str) -> str:
    """Convert `PT2H0M20S` to readable time."""
    if "H" in duration:
        time = datetime.strptime(duration, "PT%HH%MM%SS")
    elif "M" in duration:
        time = datetime.strptime(duration, "PT%MM%SS")
    else:
        time = datetime.strptime(duration, "PT%SS")

    return str(time.time())


def create_report_data_to_show(report_data: list[dict]) -> tuple:
    """Create needed view for report file."""
    all_info_report = []
    grouped_by_date_report = []

    for time_entry in report_data:
        try:
            duration = convert_duration_to_time_format(time_entry["duration"])
        except ValueError:
            duration = "-"

        all_info_report.append({
                    "name": time_entry["name"],
                    "description": time_entry["description"],
                    "duration": duration
                })

        grouped_by_date_report.append({
            "name": time_entry["name"],
            "date": time_entry["date"][0:10],
            "duration": duration
        })

    return all_info_report, grouped_by_date_report


def _to_int_serial_numbers_from_dict(time_entry: dict) -> list[str | int]:
    """Convert to `int` serial numbers of the dict."""
    return [_convert_to_int_if_int(c) for c in re.split(
        r'(\d+)', time_entry["name"])]


def sort_all_info_report(all_info_report: list[dict]) -> list[dict]:
    return sorted(all_info_report, key=_to_int_serial_numbers_from_dict)


def sort_grouped_by_date_report(
        grouped_by_date_report: list[dict]) -> list[dict]:
    grouped_by_date_report.reverse()
    return grouped_by_date_report


def group_report_by_date(report: list[dict]) -> list[dict]:
    """Group report data by date."""
    grouped_by_date_report = []

    for k, v in groupby(report, key=lambda x: x["date"]):
        grouped_by_date_report.append({k: list(v)})

    return grouped_by_date_report
