"""
This module is used to get needed
data from `Clockify.me` API.
"""
import json

import requests

from exceptions import ApplicationError

CLOCKIFY_API_URL = "https://api.clockify.me/api/v1"


def get_all_project_tasks(
        clockify_api_key: str, workspace_id: str, project_id: str
) -> list[dict]:
    """Take all tasks of the project using its id."""
    url = (
        f"{CLOCKIFY_API_URL}/workspaces/{workspace_id}"
        f"/projects/{project_id}/tasks"
    )

    headers = {
        "content-type": "application/json",
        "X-Api-Key": clockify_api_key
    }

    response = requests.get(url=url, headers=headers)

    try:
        project_tasks = json.loads(response.content)
    except json.decoder.JSONDecodeError:
        raise ApplicationError("Sorry, something wrong with API =(")

    return project_tasks
