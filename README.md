# Project README

## Introduction
This project is an example of a simple test suite for a To-Do application's API that aims to showcase some of the good practices when creating simple API test automation project. It includes test cases to verify various functionalities such as creating, updating, listing, and deleting tasks. The tests are written in Python using the pytest framework and utilize the requests library for making API calls. Additionally, the Allure framework is integrated for test reporting.

Please feel free to ping me for any comments on simple improvments. (igor13trifunovic@gmail.com)

## Files Included
- `test_todo.py`: Contains the test cases written in Python using the pytest framework.
- `api_helper.py`: Provides helper functions to interact with the To-Do application's API.

## Dependencies
```bash
pip install -r requirements.txt
```

## Test Cases Overview
- test_can_call_endpoint: Verifies if the API endpoint can be called successfully.
- test_can_create_task_mock: Tests the creation of a new task using mock response.
- test_can_create_task: Tests the creation of a new task.
- test_can_update_task: Tests the updating of an existing task.
- test_can_list_tasks: Verifies if tasks can be listed for a specific user.
- test_can_delete_task: Tests the deletion of a task.

## Test Run Command
To execute the test suite, use the following command:
```bash
pytest test_todo.py --alluredir=results
```
## Allure Installation and Environment Configuration

To generate test reports with Allure, follow these steps:

1. **Install Allure**:
   - Visit the [Allure Framework Releases page](https://github.com/allure-framework/allure2/releases) and download the latest version of Allure for your operating system (Windows, Linux, or macOS).
   - Extract the downloaded file to a directory of your choice.

2. **Add Allure to the System Path**:
   - Add the directory containing the Allure executable to your system's PATH environment variable.
     - On Windows, you can do this by adding the directory to the PATH through the System Properties or using a command like `setx PATH "%PATH%;C:\path\to\allure\bin"`.
     - On Linux/macOS, you can add it to the PATH in your shell's configuration file (e.g., `.bashrc`, `.zshrc`).

3. **Verify Allure Installation**:
   - Open a new terminal window and run the following command to verify that Allure is installed and configured correctly:
     ```bash
     allure --version
     ```

Once Allure is installed and added to the system PATH, you can generate test reports by running your test suite and then using Allure commands to generate the reports.


## Allure Command for HTML Reports
After running the tests, generate HTML reports using the following command:
```bash
allure generate --single-file results
```
After this allure-report/index.html file will contain all results generated inside /results folder and it can be send independently. 

## TODO

- [ ] Improve documentation for helper functions.
- [ ] Create new APIs (where create_task will use POST method).
- [x] Add more test cases for edge cases.
- [x] Update the installation instructions with additional configuration steps for configuring Allure.


### Contributor:
[Igor Trifunovic](https://github.com/IgorTrifunovic)