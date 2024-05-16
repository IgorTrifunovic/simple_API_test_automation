import requests
from api_helper import ApiHelper
from allure import step

class Test_ToDo:
    def setup_class(self):
        self.api_helper = ApiHelper()
        
    @step("Calling API endpoint")
    def test_can_call_endpoint(self):
        response = requests.get(self.api_helper.ENDPOINT)
        assert response.status_code == 200
        
    @step("Creating a new task (mock)")
    def test_can_create_task_mock(self):
        payload = self.api_helper.new_task_payload()
        create_task_response = self.api_helper.create_task_mock(payload)
        assert create_task_response.status_code == 201
        data = create_task_response.json()
        task_id = data["task"]["task_id"]
        assert task_id == "mock_task_id"
        
    @step("Creating a new task")
    def test_can_create_task(self):
        payload = self.api_helper.new_task_payload()
        create_task_response = self.api_helper.create_task(payload)
        assert create_task_response.status_code == 200
        data = create_task_response.json()
        task_id = data["task"]["task_id"]
        print("\n", task_id)
        get_task_response = self.api_helper.get_task(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == payload["content"]
        assert get_task_data["user_id"] == payload["user_id"]
        assert get_task_data["task_id"] == task_id
        
    @step("Updating a task")
    def  test_can_update_task(self):
        payload = self.api_helper.new_task_payload()
        create_task_response = self.api_helper.create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()["task"]["task_id"]

        new_payload = {
            "user_id": payload["user_id"],
            "task_id": task_id,
            "content": "My UPDATED content",
            "is_done": True,
        }
        
        update_task_response = self.api_helper.update_task(new_payload)
        assert update_task_response.status_code == 200
        get_task_response = self.api_helper.get_task(task_id)
        assert get_task_response.status_code == 200
        get_task_data = get_task_response.json()
        assert get_task_data["content"] == new_payload["content"]
        assert get_task_data["is_done"] == new_payload["is_done"]
        
    @step("Listing a task")
    def test_can_list_tasks(self):
        n = 3
        payload = self.api_helper.new_task_payload()
        for _ in range(n):
            create_task_response = self.api_helper.create_task(payload)
            assert create_task_response.status_code == 200
        
        user_id = payload['user_id']
        list_tasks_response = self.api_helper.list_tasks(user_id)
        assert list_tasks_response.status_code == 200
        data = list_tasks_response.json()
        tasks = data['tasks']
        assert len(tasks) == n
        print(data)
        
    @step("Delete a task")
    def test_can_delete_task(self):
        payload = self.api_helper.new_task_payload()
        create_task_response = self.api_helper.create_task(payload)
        assert create_task_response.status_code == 200
        task_id = create_task_response.json()['task']['task_id']
        delete_task_response = self.api_helper.delete_task(task_id)
        assert delete_task_response.status_code == 200
        get_task_response = self.api_helper.get_task(task_id)
        assert get_task_response.status_code == 404
        