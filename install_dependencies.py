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

def install_dependencies():
    # Install dependencies from requirements.txt file
    subprocess.run(['pip', 'install', '-r', 'requirements.txt'])


if __name__ == "__main__":
    # Install dependencies
    try:
        install_dependencies()
        
        # Run the server
        server_process = run_server()

        # Wait for the server to start (adjust sleep time as needed)
        time.sleep(2)
    finally:
        # Stop the server
        stop_server(server_process)
