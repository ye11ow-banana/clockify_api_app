"""
This module is the entry point of the application.
"""
import os

import api_service
import formatter
import views


def task6(
        workspace_id: str, project_id: str,
        clockify_api_key: str) -> list[dict]:
    """Implement needed functional for `task 6`."""
    url = api_service.create_url_to_get_all_project_tasks(
        workspace_id, project_id)
    tasks = api_service.send_GET_request_to_API(url, clockify_api_key)

    tasks_names = formatter.pull_out_tasks_names(tasks)
    tasks_names = formatter.sort_tasks_names_by_serial_numbers(tasks_names)

    views.print_list_elements(tasks_names)

    return tasks


def task8(
        workspace_id: str, user_id: str,
        clockify_api_key: str, tasks: list[dict]) -> None:
    """Implement needed functional for `task 8`."""
    url = api_service.create_url_to_get_all_time_entries(
        workspace_id, user_id)
    time_entries = api_service.send_GET_request_to_API(url, clockify_api_key)

    report_data = formatter.pull_out_report_data(tasks, time_entries)
    report_data_to_show = formatter.create_report_data_to_show(report_data)

    all_info_report = formatter.sort_all_info_report(
        report_data_to_show[0].copy())
    grouped_by_date_report = formatter.sort_grouped_by_date_report(
        report_data_to_show[1].copy())

    grouped_by_date_report = formatter.group_report_by_date(
        grouped_by_date_report)

    excel_report = views.ExcelReporter("report.xlsx")
    excel_report.create_report_file(all_info_report, grouped_by_date_report)


def main() -> None:
    """Entry point to the application."""
    CLOCKIFY_API_KEY = os.getenv("CLOCKIFY_API_KEY", "")
    WORKSPACE_ID = os.getenv("WORKSPACE_ID", "")
    PROJECT_ID = os.getenv("PROJECT_ID", "")
    USER_ID = os.getenv("USER_ID", "")

    tasks = task6(WORKSPACE_ID, PROJECT_ID, CLOCKIFY_API_KEY)
    task8(WORKSPACE_ID, USER_ID, CLOCKIFY_API_KEY, tasks)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        views.show_error_message(str(e))
