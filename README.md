# ttm
Here's a concise and to-the-point README for the provided code:

---

# Project Overview

## Folder Structure

The project follows a specific folder structure to organize the code:

- `backend`: Contains the backend code for the FastAPI server and related modules.
- `tests`: Contains the test cases for the backend code.
- `config`: Contains configuration files used by the application.
- `data_store`: Stores data files used by the application.

All Python scripts, including the FastAPI server (`main.py`), are located within the `backend` directory. Test cases are located in the `tests` directory.

## Project Setup

### Virtual Environment Creation:

To create a virtual environment named `venv`, run the following command:
- python3 -m venv venv
- cd path/to/project/myenv
- source bin/activate




### Python Path Setup:

To ensure that Python can find modules and packages in your project directory, you can add the project's directory to the Python path. Run the following command:

- please use the **absolute path of your environment** below is a structure in my local env in macOS

- **macOS / Linux:**

export PYTHONPATH="/Volumes/user/TTM_Project/ttm/:$PYTHONPATH"


- **Windows:**

set PYTHONPATH="/Volumes/user/TTM_Project/ttm/;%PYTHONPATH%"

This command adds the `backend` directory to the Python path, allowing Python to locate modules and packages within that directory.

- **SAMPLE OUTPUT of path check:**
(venv) AKs:ttm user$ echo $PYTHONPATH
/Volumes/user/TTM_Project/ttm/:


### IMPORTANT PATH CHANGES TO DATA STORE
- ./backend/config/ holds config.ini and constants.py to handle generic data retrieval
- Current path is set to my local repo as shown below please change as per your pwd or present working directory.
- WorkingCapitalData = **/Volumes/arun/TTM_Project/ttm**/backend/data_store/working_capital.csv
- PNLData = **/Volumes/arun/TTM_Project/ttm/**/backend/data_store/pnl.csv
- Change above to point to your data store path
- Under constants.py please make similar change to point a the correct config.ini location as shown below
- _config_file = "**/Volumes/arun/TTM_Project/ttm/**/backend/config/config.ini"



## FastAPI Server and Test Automation

This script install_dependencies_and_run_tests.py automates the setup, testing, and coverage reporting for a FastAPI server using Python.

### Features:

- **Server Management:**
  - Starts the FastAPI server in a separate process.
  - Gracefully stops the server after running tests.

- **Test Automation:**
  - Installs project dependencies from `requirements.txt` with the use of a wrapper module `install_dependencies.py`.
  - Runs pytest with coverage to test the backend code with the use of a wrapper module `run_coverage.py`.
  - Generates an HTML coverage report can be run at terminal by : `open ./tests/htmlcov/index.html` navigate to the base path of the project.

### ################################################################################################################################################################

### Project Setup:
1. **Setup:**
   - Ensure Python and pip are installed.
   - Install project dependencies `python install_dependencies.py` or `pip install -r requirements.txt`.

## Configuration

### Configuring Paths

- **config.ini:** 
  - The `config.ini` file contains paths to important data files location : `./backend/config/` from base path. 
  - Open the `config.ini` file and update the paths in the `[Paths]` section to point to the relevant file locations. 
  - Ensure that the paths are updated according to your file structure.

### Constants Configuration

- **constants.py:**
  - The `constants.py` file defines certain constants used throughout the application, location : `./backend/config/` from base path. 
  - Open the `constants.py` file and update the `_config_file` path if necessary to point to the correct full location of the configuration file.
  - Modify the path as needed to match your file structure.


## FastAPI Server

### Running Application

To run the FastAPI application:

1. Ensure that all dependencies are installed. You can install them following steps under "Project Setup":

2. Run the FastAPI server by executing the `python ./backend/main.py` from base path of the project.

3. Once the server is running, you can access the API endpoints. By default, the server will be hosted at `http://localhost:8000`.

4. You can use tools like cURL or Postman to make requests to the API endpoints. For example:

    ```
    curl -X GET "http://localhost:8000/cash-flow/?analysis_type=monthly&start_date=2019-01-01&more_info=True"
    ```

5. Remember to stop the server once you're done testing by pressing `Ctrl + C` in the terminal.


### TESTING Usage:

1. **Test Setup:**
   - Ensure Python and pip are installed.
   - Install project dependencies if not installed using `python install_dependencies.py`.
   - run all the tests to generate performance analysis on terminal and coverage report: `python run_coverage.py`.

2. **Testing and Coverage:**
   - Above steps will run all the filename.*_test.py located in project
   - HTML coverage report will be saved and ready to be viewed with the default web browser.
   - To view the html execute : `open ./tests/htmlcov/index.html`.

3. **Cleanup:**
   - The server process is stopped automatically after testing.

### Notes:

- Adjust the sleep time (`time.sleep()`) in the script if needed for the server to start properly.
- Ensure the correct paths are configured for server and coverage report files.

--- 

