import subprocess
import webbrowser
import time

def run_server():
    # Run the FastAPI server in a separate process
    server_process = subprocess.Popen(["python", "./backend/main.py"])
    return server_process

def stop_server(server_process):
    # Kill the server process
    server_process.kill()

def run_tests_and_generate_coverage():
    # Run pytest with coverage and generate HTML report
    subprocess.run(['pytest', '--cov=./backend/', './tests/backend/', '--capture=tee-sys'])

def open_coverage_report_in_browser():
    # Open the HTML coverage report in the default web browser
    webbrowser.open_new_tab('./htmlcov/index.html')

if __name__ == "__main__":
    
    try:
        # Run the server    
        server_process = run_server()

        # Wait for the server to start (adjust sleep time as needed)
        time.sleep(2)
        # Run tests and generate coverage
        run_tests_and_generate_coverage()

        # Open coverage report in browser
        open_coverage_report_in_browser()
    except Exception as e:
        print("An error occurred:", e)
        
    finally:
        # Stop the server
        stop_server(server_process)
