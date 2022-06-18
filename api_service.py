"""
This module is used to get needed
data from `Clockify.me` API.
"""
import json

import requests

from exceptions import ApplicationError

CLOCKIFY_API_URL = "https://api.clockify.me/api/v1"


def send_GET_request_to_API(url: str, clockify_api_key: str) -> list[dict]:
    """Send GET request to `Clockify.me` API."""
    headers = {
        "content-type": "application/json",
        "X-Api-Key": clockify_api_key
    }

    response = requests.get(url=url, headers=headers)

    try:
        response_data = json.loads(response.content)
    except json.decoder.JSONDecodeError:
        raise ApplicationError("Sorry, something wrong with API =(")

    return response_data


def create_url_to_get_all_project_tasks(
        workspace_id: str, project_id: str) -> str:
    """Create url to take all tasks of the project using its id."""
    return (
        f"{CLOCKIFY_API_URL}/workspaces/{workspace_id}"
        f"/projects/{project_id}/tasks"
    )


def create_url_to_get_all_time_entries(workspace_id: str, user_id: str) -> str:
    """Create url to take all time entries of user."""
    return (
        f"{CLOCKIFY_API_URL}/workspaces/{workspace_id}"
        f"/user/{user_id}/time-entries"
    )
