import requests
import uuid
import unittest.mock


class ApiHelper:
    ENDPOINT = "https://todo.pixegami.io"
    def __init__(self):
        pass
    
    def create_task_mock(self, payload):
        mock_response = unittest.mock.Mock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"task": {"task_id": "mock_task_id"}}
        return mock_response
    
    def create_task(self, payload):
        return requests.put(self.ENDPOINT + "/create-task", json=payload)

    def update_task(self, payload):
        return requests.put(self.ENDPOINT + "/update-task", json=payload)

    def get_task(self, task_id):
        return requests.get(self.ENDPOINT + f"/get-task/{task_id}")

    def new_task_payload(self):
        user_id = f"test_user_{uuid.uuid4().hex}"
        content = f"test_content_{uuid.uuid4().hex}"
        print(f"Creating task for user {user_id} with content {content}")
        return {
            "content": content,
            "user_id": user_id,
            "is_done": False,
        }

    def list_tasks(self, user_id):
        return requests.get(self.ENDPOINT + f"/list-tasks/{user_id}")

    def delete_task(self, task_id):
        return requests.delete(self.ENDPOINT + f"/delete-task/{task_id}")
    