"""
This module is the entry point of the application.
"""
import os

import api_service
import formatter
import views


def main() -> None:
    CLOCKIFY_API_KEY = os.getenv("CLOCKIFY_API_KEY", "")
    WORKSPACE_ID = os.getenv("WORKSPACE_ID", "")
    PROJECT_ID = os.getenv("PROJECT_ID", "")

    tasks_data = api_service.get_all_project_tasks(
        CLOCKIFY_API_KEY, WORKSPACE_ID, PROJECT_ID)

    tasks = formatter.pull_out_tasks_names(tasks_data)
    tasks = formatter.filter_tasks_by_serial_number(tasks)
    views.print_list_elements(tasks)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        views.show_error_message(str(e))
