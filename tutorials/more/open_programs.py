import subprocess

# Define the applications and their paths
applications = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "notepad": "C:\\Windows\\System32\\notepad.exe",
}

# Open a specific application
def open_app(app_name):
    app_path = applications[app_name]
    if app_path:
        subprocess.Popen(app_path)
    else:
        print(f"Application '{app_name}' not found.")

# Example usage
app_name = input("Enter the name of the application you want to open: ")
open_app(app_name.lower())