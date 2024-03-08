# ttm
Here's a concise and to-the-point README for the provided code:

---

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
   - Install project dependencies `python install_dependencies.py`.

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

